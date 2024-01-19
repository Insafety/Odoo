 # -*- coding: utf-8 -*-
from odoo import api, models

class Partner(models.Model):
    _inherit = 'res.partner' 
    @api.model_create_multi
    def create(self, value_list):
        res = super(Partner, self).create(value_list)
        p = self.env['res.partner'].search(
                domain=[('id', '=', res.id)]
            )
        partner = self.buildPartnerObject(p)
        db = self.env['insafety.firebase.sync'].get_firebase()
        _docPath = self.env['insafety.firebase.sync'].get_doc_path() 
        db.document(_docPath + str(res.id)).set(partner)
        return res 
    
    def write(self, vals): 
        res = super(Partner, self).write(vals)    
        db = self.env['insafety.firebase.sync'].get_firebase()    
        _docPath = self.env['insafety.firebase.sync'].get_doc_path() 
        if db.document(_docPath + str(self.id)).get().exists:
            p = self.env['res.partner'].search(
                domain=[('id', '=', self.id)]
            )
            partner = self.buildPartnerObject(p)         
            db.document(_docPath + str(self.id)).update(partner)
        return res
    
    def unlink(self):
        for rec in self:
            super(Partner, rec).unlink()
            db = self.env['insafety.firebase.sync'].get_firebase()
            _docPath = self.env['insafety.firebase.sync'].get_doc_path() 
            if db.document(_docPath + str(rec.id)).get().exists:
                db.document(_docPath + str(rec.id)).delete()
    
    def buildPartnerObject(self, p):
         _avatar = False
         if p.avatar_1920:
             _avatar = p.avatar_1920.decode('utf8')
         return {
                "name": p.name,
                "active": p.active,
                "avatar": _avatar,
                "company_type": p.company_type,     
                "lang": p.lang,
                "is_company": p.is_company,
                "commercial_partner_id": p.commercial_partner_id.id,
                "company_id": p.company_id.id,
                "country_code": p.country_code,
                "company_type": p.company_type,
                "parent_id": p.parent_id.id,
                "contact_address": p.contact_address,
                "function": p.function,
                "phone": p.phone,
                "mobile": p.mobile,
                "email": p.email,
                "website": p.website,
                "title": p.title.display_name,
                "lang": p.lang,
                "category_ids": p.category_id.ids
            }
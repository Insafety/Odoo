# -*- coding: utf-8 -*-
from odoo import models, fields, api
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from odoo.modules.module import get_module_resource

_docPathPartners = "odoo/Insafety/Partners/"

class insafety_firebase_sync(models.Model):
    _name = 'insafety.firebase.sync'
    _description = 'Firebase Sync for Releshi'
    
    name = fields.Char(string="Name", required=True)
    if not firebase_admin._apps:
        json_file_path = get_module_resource('insafety_firebase_sync','static/src','firebase.json')
        cred = credentials.Certificate(json_file_path)
        firebaseApp = firebase_admin.initialize_app(cred)

    global db 
    db = firestore.client()

    def sync_partners(self):
        partners = self.env['res.partner'].search([],limit=1)
        for p in partners:
            partner = {
                "name": p.name,
                "active": p.active,
                "avatar": p.avatar_1920.decode('utf8'),
                "company_type": p.company_type,     
                "lang": p.lang,
                "bank_account_count": p.bank_account_count,
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
            print(p.name)
            try:
                db.document(_docPathPartners + str(p.id)).set(partner)
            except:
                print(partner)

    def delete_partners(self):
        partners = self.env['res.partner'].search([])
        for p in partners:
            try:
                db.document(_docPathPartners + str(p.id)).delete()
            except:
                print(p)


# -*- coding: utf-8 -*-
from odoo import models, fields, api
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from odoo.modules.module import get_module_resource
import json
from odoo.exceptions import ValidationError

class insafety_firebase_sync(models.Model):
    _name = 'insafety.firebase.sync'
    _description = 'Firebase Data Synch'
    
    name = fields.Char(string="Name", required=True, readonly=True)
    firebase_credentials = fields.Text(string="Firebase Project Credentials", required=True)
    firebase_doc_path = fields.Char(string="Firebase Document Path", required=True)

    def sync_partners(self):
        partners = self.env['res.partner'].search([])
        _db = self.get_firebase()
        _docPathPartners = self.get_doc_path()
        for p in partners:
            partner = self.env['res.partner'].buildPartnerObject(p)
            _doc = _docPathPartners + str(p.id)
            try:  
                _db.document(_doc).set(partner)
            except:
                raise ValidationError("Connot Set Document: " + _doc)

    def delete_partners(self):
        _partners = self.env['res.partner'].search([])
        _db = self.get_firebase()
        _docPathPartners = self.get_doc_path()
        for p in _partners:
            _doc = _docPathPartners + str(p.id)
            try:
                _db.document(_doc).delete()
            except:
                raise ValidationError("Connot Delete Document: " + _doc)
    
    def reset_connection(self):
        if firebase_admin._apps:
            firebase_admin.delete_app(firebase_admin.get_app())

    def get_firebase(self):
        if not firebase_admin._apps:
            _partner = self.env['insafety.firebase.sync'].search([('name', '=', "Partners")])
            try:
                _cert = credentials.Certificate(json.loads(_partner.firebase_credentials,strict=False))
                firebase_admin.initialize_app(_cert)
            except:
                raise ValidationError("The Firebase Credentials is not valid.")
        return firestore.client()

    def get_doc_path(self):
        _partner = self.env['insafety.firebase.sync'].search([('name', '=', "Partners")])
        return _partner.firebase_doc_path
        

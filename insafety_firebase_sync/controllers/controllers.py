# -*- coding: utf-8 -*-
# from odoo import http


# class InsafetyFirebaseSync(http.Controller):
#     @http.route('/insafety_firebase_sync/insafety_firebase_sync', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/insafety_firebase_sync/insafety_firebase_sync/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('insafety_firebase_sync.listing', {
#             'root': '/insafety_firebase_sync/insafety_firebase_sync',
#             'objects': http.request.env['insafety_firebase_sync.insafety_firebase_sync'].search([]),
#         })

#     @http.route('/insafety_firebase_sync/insafety_firebase_sync/objects/<model("insafety_firebase_sync.insafety_firebase_sync"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('insafety_firebase_sync.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
{
    'name': "insafety_firebase_sync",

    'summary': """
        Shows how to real-time synch Odoo data to Google Cloud Firebase""",

    'description': """
        Demonstrate how the eCommerce Categories and the related products 
        can be synched to Insafety's Releshi Android and iOS App. 
    """,

    'author': "Insafety GmbH, Zürich, Switzerland",
    'website': "https://odoo.insafety.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': "LGPL-3",
}

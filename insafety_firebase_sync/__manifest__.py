
# -*- coding: utf-8 -*-
{
    'name': "Insafety Firebase Sync",

    'summary': """
        Real-time synch Odoo data to Google Cloud Firebase
        """,

    'description': """
        Demonstrate how the Odoo Partners can be Real Time Synchronized to Firestore. 
        When updating, inserting or deleting Partner Data in Odoo, 
        the corresponding Firestore documents will be updated in real time.
    """,

    'author': "Insafety GmbH, Zürich, Switzerland",
    'website': "https://odoo.insafety.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'license': "LGPL-3",
    'images': ['static/description/main_screenshot.png','static/description/main_screenshot.png'],
    'module_type': 'official'
}
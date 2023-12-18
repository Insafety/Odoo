# -*- coding: utf-8 -*-
{
    'name': "insafety_property_rent",

    'summary': """
        Deals with the accounting aspects of property rentals""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Insafety GmbH, Zürich, Switzerland",
    'website': "https://odoo.insafety.ch",

    'category': 'Accounting',
    'version': '0.1',

    'depends': ['contacts','account','l10n_generic_coa','mail'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/property.xml',
        'views/property_building.xml',
        'views/property_type.xml',
        'views/property_tag.xml',
        'views/property_rent_log.xml',
        'views/property_account_view.xml',
        'views/property_rent_contract.xml',
        'views/property_analytics.xml',
        'views/menu_items.xml',
        'data/ir_cron_data.xml',
    ],

    'demo': [
        'data/demo.xml', 
    ],
    'auto_install': True,
    'license': "LGPL-3",
    'immages': ['static/cover.png'],
}

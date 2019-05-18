# -*- coding: utf-8 -*-
{
    'name': "hospitality_services",

    'summary': """
        The Suite Life of NYC 1""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://maps.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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

    'application': True
}
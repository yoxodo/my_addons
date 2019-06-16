# -*- coding: utf-8 -*-
{
    'name': "One2many checkbox",

    'summary': """
        Make One2many list in form view selectable""",

    'description': """
        Make One2many list in form view selectable
    """,

    'author': "Thành Loyal",
    'website': "http://nodo.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '11.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'price': 10.00,
    'currency': 'EUR',
    'license': 'OPL-1',
    'support': 'thanhnt@nodo.vn'
}
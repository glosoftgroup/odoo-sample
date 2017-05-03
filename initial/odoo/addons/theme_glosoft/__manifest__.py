# -*- coding: utf-8 -*-
{
    'name': "glo-theme",

    'summary': """
        E-Commerce Home
        E-Commerce Products""",

    'description': """
        This is a theme for the e-commerce website. Overriding the default look and feel
    """,

    'author': "Glosoft Theme",
    'website': "http://www.glosoftgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Theme/Site',
    'version': '0.1',
    'application':'true',

    # any module necessary for this one to work correctly
    'depends': ['website', 'sale','website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/layout.xml',
        'views/pages.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
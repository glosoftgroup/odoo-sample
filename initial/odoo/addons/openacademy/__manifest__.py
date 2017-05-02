# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Manage Trainings""",

    'description': """
         Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "GlosoftGroup",
    'website': "http://www.glosoftgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',#contains action and the menu triggering action
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
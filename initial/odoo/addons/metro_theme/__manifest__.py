# -*- coding: utf-8 -*-
# Copyright 2016 Woowebsite, LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Metro Theme",
    "summary": "Odoo 10.0 community backend theme",
    "version": "1.0",
    "category": "Themes/Backend",
    "website": "http://www.woowebsite.com",
	"description": """
		Backend theme for Odoo 10.0 community edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "Woowebsite",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
    "qweb":[
        'views/qweb.xml',
    ],
    "auto_install": False,
    "application": False,
    "price": 0.00,
}


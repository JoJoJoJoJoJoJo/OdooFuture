# -*- coding: utf-8 -*-
{
    'name': 'Maintenance Extra',
    'version': '1.0',
    'category': 'Manufacturing/Maintenance',
    # 'sequence': 50,
    'summary': 'Maintenance Extra',
    'description': """

This module allows Maintenance Extra.

""",
    'depends': ['maintenance','purchase','product'],

    'data': [
        'security/ir.model.access.csv',
        'views/maintenance_views.xml',
        'views/product_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}

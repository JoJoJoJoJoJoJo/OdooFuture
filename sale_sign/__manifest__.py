# -*- coding: utf-8 -*-


{
    'name': 'Sales Sign',
    'version': '15.0.0.0.0',
    'category': 'Sales/Sales',
    'summary': 'Send sales documents to sign',
    'description': """
    Sign documents from sales online.
    """,
    'depends': ['sale', 'sign'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

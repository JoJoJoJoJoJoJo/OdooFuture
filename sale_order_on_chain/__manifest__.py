# © 2020 Elico Corp (www.elico-corp.com).
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Order On-chain',
    'summary': 'Sale Order On-chain',
    'version': '13.0.1.0.0',
    'category': 'Sales',
    'website': 'https://www.elico-corp.com',
    'author': 'Elico Corp',
    'license': 'Other proprietary',
    'support': 'support@elico-corp.com',
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/sale_order_views.xml',
        'wizards/on_chain_wizard_views.xml',
    ],
    'application': False,
    'installable': True,
}

# © 2020 Elico Corp (www.elico-corp.com).
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class OnChainWizard(models.TransientModel):
    _name = "on.chain.wizard"

    order_ids = fields.Many2many(
        'sale.order',
        readonly=True,
    )

    @api.model
    def default_get(self, fields):
        res = super(OnChainWizard, self).default_get(fields)
        active_ds = self.env.context.get('active_ids')
        order_ids = self.env['sale.order'].browse(active_ds)
        order_names = []
        for order in order_ids:
            if order.state != 'sale' or order.txid != False:
                order_names.append(order.name)
        if order_names:
            raise UserError('{} can not be on-chain!'.format(','.join(order_names)))
        res.update({
            'order_ids': active_ds  ,
        })
        return res

    def action_on_chain(self):
        self.ensure_one()
        self.order_ids.action_order_on_chain()

# © 2020 Elico Corp (www.elico-corp.com).
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class BlockChainConfig(models.Model):
    _name = "block.chain.config"

    sale_order_url = fields.Char(
        required=True,
    )

    sale_order_line_url = fields.Char(
        required=True,
    )
    active = fields.Boolean(default=True)

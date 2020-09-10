# © 2020 Elico Corp (www.elico-corp.com).
# See LICENSE file for full copyright and licensing details.


from odoo import models, fields


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    company = fields.Char()
    job = fields.Char(
        "Job Position",
    )

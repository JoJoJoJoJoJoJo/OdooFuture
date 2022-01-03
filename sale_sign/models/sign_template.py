from odoo import fields, models


class SignTemplate(models.Model):
    _inherit = 'sign.template'

    res_model = fields.Char('Model name')
    res_id = fields.Many2oneReference(string='Record ID', help="ID of the target record in the database", model_field='res_model')

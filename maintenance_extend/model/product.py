from odoo import api, fields, models


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    website = fields.Char('website', help="Website of the product")
    equipment_count = fields.Integer('Equipment Count', compute='_compute_equipment')
    equipment_ids = fields.Many2many('maintenance.equipment', string='Equipments', compute='_compute_equipment')

    def _compute_equipment(self):
        for rec in self:
            equipment_lines = self.env['maintenance.order.line'].search([('product_id', '=', rec.id)])
            equipment_ids = equipment_lines.mapped('order_id')
            rec.equipment_ids = equipment_ids.ids
            rec.equipment_count = len(equipment_ids)

    def action_view_eq(self):
        action = self.env["ir.actions.actions"]._for_xml_id("maintenance.hr_equipment_action")
        action['domain'] = [('id', 'in', self.equipment_ids.ids)]
        return action

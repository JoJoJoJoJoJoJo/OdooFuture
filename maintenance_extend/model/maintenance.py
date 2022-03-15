from odoo import api, fields, models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    supplier_order = fields.Char('supplier_order')
    production_check_date = fields.Date('production check date')
    engine_sn = fields.Char('engine_sn')
    drive_sn = fields.Char('drive_sn')
    transmission_sn = fields.Char('transmission_sn')
    frame_sn = fields.Char('frame_sn')
    attachment_name = fields.Char('attachment_name')
    attachment_sn = fields.Char('attachment_sn')
    tire_sn = fields.Char('tire_sn')

    order_line = fields.One2many('maintenance.order.line', 'order_id', string='Order Lines', copy=True)


class MaintenanceOrderLine(models.Model):
    _name = 'maintenance.order.line'
    _description = 'Maintenance Order Line'
    _order = 'order_id, id'

    order_id = fields.Many2one('maintenance.equipment', string='Maintenance Order Reference', index=True, required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', change_default=True)
    default_code = fields.Char('Default Code', related='product_id.default_code')
    website = fields.Char('Website', related='product_id.website', help="Website of the product")

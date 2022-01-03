from odoo import fields, models
import base64


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def send_report_to_sign(self):
        report = self.env['ir.actions.report']._get_report_from_name('sale.report_saleorder')
        pdf, _type = report._render_qweb_pdf(self.ids)
        attachment_vals = {
            'name': report.name,
            'datas': base64.b64encode(pdf),
            'res_model': self._name,
            'res_id': self.id,
            'type': 'binary',
        }
        attachment = self.env['ir.attachment'].create(attachment_vals)
        sign_template = self.env['sign.template'].create({
            'attachment_id': attachment.id,
            'tag_ids': [(6, 0, self.env.ref('sign.sign_template_tag_3').ids)],
            'res_model': self._name,
            'res_id': self.id,
        })
        action = self.env['ir.actions.act_window']._for_xml_id('sign.sign_template_action')
        action['domain'] = [('id', '=', sign_template.id)]
        return action

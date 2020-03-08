# © 2020 Elico Corp (www.elico-corp.com).
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import requests
import json
import datetime

TIMEOUT = 10
SALE_ORDER_INIT = 'http://fuchain.nat300.top/odoo/salesorder/initMember'
SALE_ORDER_LINE_INIT = 'http://fuchain.nat300.top/odoo/salesorderlines/initMember'


def on_chain(endpoint, data, odoo_id):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    json_data = {
        'jsonObject': json.dumps(data)
    }
    req = requests.post(endpoint, data=json_data, headers=headers, timeout=TIMEOUT)
    req.raise_for_status()
    content = json.loads(req.content)
    if content.get('code') == 200:
        odoo_id.txid = content.get('txid')
        odoo_id.write({
            'txid': content.get('txid'),
            'on_chain_id': data.get('id'),
        })
    else:
        raise ValidationError(content.get('error'))


class SaleOrder(models.Model):
    _inherit = "sale.order"

    txid = fields.Char(
        copy=False,
    )
    on_chain_id = fields.Char(
        copy=False,
    )

    def action_order_on_chain(self):
        for order in self:
            if order.txid:
                raise UserError('The order is on-chain!')
            order_data = {
                "write_date": order.write_date and order.write_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT) or '',
                "auto_purchase_order_id": "AUTO_PURCHASE_ORDER_ID",
                "expense_ids": "EXPENSE_IDS",
                "invoice_ids": "INVOICE_IDS",
                "is_abandoned_cart": "IS_ABANDONED_CART",
                "message_main_attachment_id": order.message_main_attachment_id.name or '',
                "validity_date": order.validity_date and order.validity_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT) or '',
                "amount_total": str(order.amount_total),
                "promo_code": "PROMO_CODE",
                "warning_stock": "WARNING_STOCK",
                "activity_date_deadline": "ACTIVITY_DATE_DEADLINE",
                "team_id": order.team_id.name or '',
                "message_channel_ids": "MESSAGE_CHANNEL_IDS",
                "activity_state": "ACTIVITY_STATE",
                "auto_generated": "AUTO_GENERATED",
                "message_has_error_counter": "MESSAGE_HAS_ERROR_COUNTER",
                "purchase_order_count": "PURCHASE_ORDER_COUNT",
                "next_action_date": "NEXT_ACTION_DATE",
                "amount_by_group": "AMOUNT_BY_GROUP",
                "effective_date": "EFFECTIVE_DATE",
                "id": datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(order.id),
                "state": order.state or '',
                "picking_policy": "PICKING_POLICY",
                "margin": "MARGIN",
                "message_attachment_count": "MESSAGE_ATTACHMENT_COUNT",
                "tag_ids": "TAG_IDS",
                "client_order_ref": order.client_order_ref or '',
                "pricelist_id": order.pricelist_id.name or '',
                "picking_ids": "PICKING_IDS",
                "create_uid": order.create_uid.name or '',
                "cart_quantity": "CART_QUANTITY",
                "access_token": order.access_token or '',
                "code_promo_program_id": "CODE_PROMO_PROGRAM_ID",
                "access_warning": "ACCESS_WARNING",
                "user_id": order.user_id.name or '',
                "partner_invoice_id": order.partner_invoice_id.name or '',
                "delivery_rating_success": "DELIVERY_RATING_SUCCESS",
                "delivery_set": "DELIVERY_SET",
                "generated_coupon_ids": "GENERATED_COUPON_IDS",
                "message_is_follower": "MESSAGE_IS_FOLLOWER",
                "reward_amount": "REWARD_AMOUNT",
                "require_payment": str(order.require_payment),
                "signature": "SIGNATURE",
                "rental_status": "RENTAL_STATUS",
                "expense_count": "EXPENSE_COUNT",
                "has_returnable_lines": "HAS_RETURNABLE_LINES",
                "commitment_date": order.commitment_date and order.commitment_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT) or '',
                "currency_rate": str(order.currency_rate),
                "amount_tax": str(order.amount_tax),
                "amount_untaxed": str(order.amount_untaxed),
                "order_line": "ORDER_LINE",
                "amount_undiscounted": "AMOUNT_UNDISCOUNTED",
                "applied_coupon_ids": "APPLIED_COUPON_IDS",
                "only_services": "ONLY_SERVICES",
                "amount_delivery": "AMOUNT_DELIVERY",
                "company_id": order.company_id.name or '',
                "invoice_count": "INVOICE_COUNT",
                "message_has_sms_error": "MESSAGE_HAS_SMS_ERROR",
                "grid_product_tmpl_id": "GRID_PRODUCT_TMPL_ID",
                "is_rental_order": "IS_RENTAL_ORDER",
                "activity_type_id": "ACTIVITY_TYPE_ID",
                "is_expired": "IS_EXPIRED",
                "signed_by": order.signed_by or '',
                "grid": "GRID",
                "authorized_transaction_ids": "AUTHORIZED_TRANSACTION_IDS",
                "message_ids": "MESSAGE_IDS",
                "source_id": order.source_id.name or '',
                "warehouse_id": "WAREHOUSE_ID",
                "type_name": "TYPE_NAME",
                "message_partner_ids": "MESSAGE_PARTNER_IDS",
                "activity_exception_decoration": "ACTIVITY_EXCEPTION_DECORATION",
                "payment_term_id": order.payment_term_id.name or '',
                "reference": order.reference or '',
                "activity_ids": "ACTIVITY_IDS",
                "date_order": order.date_order and order.date_order.strftime(DEFAULT_SERVER_DATETIME_FORMAT) or '',
                "is_all_service": "IS_ALL_SERVICE",
                "analytic_account_id": order.analytic_account_id.name or '',
                "has_late_lines": "HAS_LATE_LINES",
                "report_grids": "REPORT_GRIDS",
                "transaction_ids": "TRANSACTION_IDS",
                "create_date": order.create_date and order.create_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT) or '',
                "medium_id": order.medium_id.name or '',
                "campaign_id": order.campaign_id.name or '',
                "__last_update": "__LAST_UPDATE",
                "activity_user_id": "ACTIVITY_USER_ID",
                "message_follower_ids": "MESSAGE_FOLLOWER_IDS",
                "activity_exception_icon": "ACTIVITY_EXCEPTION_ICON",
                "display_name": "DISPLAY_NAME",
                "sale_order_template_id": order.sale_order_template_id.name or '',
                "opportunity_id": "OPPORTUNITY_ID",
                "expected_date": "EXPECTED_DATE",
                "incoterm": "INCOTERM",
                "name": order.name or '',
                "website_message_ids": "WEBSITE_MESSAGE_IDS",
                "has_pickable_lines": "HAS_PICKABLE_LINES",
                "partner_shipping_id": order.partner_shipping_id.name or '',
                "website_id": "WEBSITE_ID",
                "cart_recovery_email_sent": "CART_RECOVERY_EMAIL_SENT",
                "invoice_status": order.invoice_status or '',
                "note": order.note or '',
                "delivery_message": "DELIVERY_MESSAGE",
                "write_uid": order.write_uid.name or '',
                "origin": order.origin or '',
                "fiscal_position_id": order.fiscal_position_id.name or '',
                "signed_on": order.signed_on and order.signed_on.strftime(DEFAULT_SERVER_DATETIME_FORMAT) or '',
                "delivery_count": "DELIVERY_COUNT",
                "grid_update": "GRID_UPDATE",
                "carrier_id": "CARRIER_ID",
                "message_unread": "MESSAGE_UNREAD",
                "partner_id": order.partner_id.name or '',
                "remaining_validity_days": "REMAINING_VALIDITY_DAYS",
                "sale_order_option_ids": "SALE_ORDER_OPTION_IDS",
                "require_signature": str(order.require_signature),
                "recompute_delivery_price": "RECOMPUTE_DELIVERY_PRICE",
                "access_url": "ACCESS_URL",
                "message_unread_counter": "MESSAGE_UNREAD_COUNTER",
                "website_order_line": "WEBSITE_ORDER_LINE",
                "message_has_error": "MESSAGE_HAS_ERROR",
                "procurement_group_id": "PROCUREMENT_GROUP_ID",
                "message_needaction": "MESSAGE_NEEDACTION",
                "activity_summary": "ACTIVITY_SUMMARY",
                "message_needaction_counter": "MESSAGE_NEEDACTION_COUNTER",
                "website_description": "WEBSITE_DESCRIPTION",
                "currency_id": "CURRENCY_ID",
                "no_code_promo_program_ids": "NO_CODE_PROMO_PROGRAM_IDS"}
            order.order_line.order_line_on_chain()
            on_chain(SALE_ORDER_INIT, order_data, order)

class SaleOderLine(models.Model):
    _inherit = 'sale.order.line'

    txid = fields.Char(
        copy=False,
    )
    on_chain_id = fields.Char(
        copy=False,
    )

    def order_line_on_chain(self):
        for order_line in self:
            if order_line.txid:
                raise UserError('The order line is on-chain!')
            line_data = {
                "write_date": order_line.write_date and order_line.write_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                "move_ids": "MOVE_IDS",
                "is_late": "IS_LATE",
                "qty_to_deliver": "QTY_TO_DELIVER",
                "route_id": "ROUTE_ID",
                "price_subtotal": str(order_line.price_subtotal),
                "display_qty_widget": "DISPLAY_QTY_WIDGET",
                "qty_delivered": str(order_line.qty_delivered),
                "discount": str(order_line.discount),
                "warning_stock": "WARNING_STOCK",
                "scheduled_date": "SCHEDULED_DATE",
                "salesman_id": order_line.salesman_id.name or '',
                "untaxed_amount_invoiced": str(order_line.untaxed_amount_invoiced),
                "pickup_date": "PICKUP_DATE",
                "purchase_line_ids": "PURCHASE_LINE_IDS",
                "qty_delivered_method": order_line.qty_delivered_method or '',
                "is_downpayment": str(order_line.is_downpayment),
                "option_line_ids": "OPTION_LINE_IDS",
                "is_configurable_product": "IS_CONFIGURABLE_PRODUCT",
                "rental_updatable": "RENTAL_UPDATABLE",
                "product_custom_attribute_value_ids": "PRODUCT_CUSTOM_ATTRIBUTE_VALUE_IDS",
                "product_id": order_line.product_id.name or '',
                "id": datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(order_line.id),
                "state": order_line.state,
                "create_date": order_line.create_date and order_line.create_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT) or '',
                "name_short": "NAME_SHORT",
                "untaxed_amount_to_invoice": str(order_line.untaxed_amount_to_invoice),
                "is_expense": str(order_line.is_expense),
                "margin": "MARGIN",
                "__last_update": "__LAST_UPDATE",
                "is_reward_line": "IS_REWARD_LINE",
                "product_template_attribute_value_ids": "PRODUCT_TEMPLATE_ATTRIBUTE_VALUE_IDS",
                "customer_lead": str(order_line.customer_lead),
                "linked_line_id": "LINKED_LINE_ID",
                "purchase_line_count": "PURCHASE_LINE_COUNT",
                "create_uid": order_line.create_uid.name or '',
                "display_name": "DISPLAY_NAME",
                "is_delivery": "IS_DELIVERY",
                "analytic_tag_ids": "ANALYTIC_TAG_IDS",
                "is_rental": "IS_RENTAL",
                "tax_id": "TAX_ID",
                "price_reduce": str(order_line.price_reduce),
                "sequence": str(order_line.sequence),
                "name": order_line.name or '',
                "purchase_price": "PURCHASE_PRICE",
                "is_mto": "IS_MTO",
                "order_id": order_line.order_id.name or '',
                "invoice_status": order_line.invoice_status or '',
                "price_total": str(order_line.price_total),
                "return_date": "RETURN_DATE",
                "price_reduce_taxexcl": str(order_line.price_reduce_taxexcl),
                "write_uid": order_line.write_uid.name or '',
                "product_template_id": "PRODUCT_TEMPLATE_ID",
                "reservation_begin": "RESERVATION_BEGIN",
                "display_type": order_line.display_type or '',
                "qty_invoiced": str(order_line.qty_invoiced),
                "is_product_rentable": "IS_PRODUCT_RENTABLE",
                "product_no_variant_attribute_value_ids": "PRODUCT_NO_VARIANT_ATTRIBUTE_VALUE_IDS",
                "price_reduce_taxinc": str(order_line.price_reduce_taxinc),
                "product_packaging": "PRODUCT_PACKAGING",
                "product_uom": order_line.product_uom.name or '',
                "sale_order_option_ids": "SALE_ORDER_OPTION_IDS",
                "virtual_available_at_date": "VIRTUAL_AVAILABLE_AT_DATE",
                "qty_to_invoice": str(order_line.qty_to_invoice),
                "qty_returned": "QTY_RETURNED",
                "company_id": order_line.company_id.name or '',
                "price_tax": str(order_line.price_tax),
                "qty_available_today": "QTY_AVAILABLE_TODAY",
                "recompute_delivery_price": "RECOMPUTE_DELIVERY_PRICE",
                "order_partner_id": order_line.order_partner_id.name or '',
                "free_qty_today": "FREE_QTY_TODAY",
                "price_unit": str(order_line.price_unit),
                "product_type": "PRODUCT_TYPE",
                "product_updatable": "PRODUCT_UPDATABLE",
                "qty_delivered_manual": str(order_line.qty_delivered_manual),
                "website_description": "WEBSITE_DESCRIPTION",
                "product_qty": "PRODUCT_QTY",
                "analytic_line_ids": "ANALYTIC_LINE_IDS",
                "invoice_lines": "INVOICE_LINES",
                "currency_id": order_line.currency_id.name or '',
                "product_uom_category_id": "PRODUCT_UOM_CATEGORY_ID",
                "product_uom_qty": str(order_line.product_uom_qty),
                "warehouse_id": "WAREHOUSE_ID"
            }
            on_chain(SALE_ORDER_LINE_INIT ,line_data, order_line)

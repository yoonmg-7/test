from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    warranty_id = fields.Many2one(
        'product.warranty',
        string='Warranty',
        related='product_template_id.warranty_id',
        store=True,
    )

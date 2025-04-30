from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # capacity_id = fields.Many2one('product.capacity', string='Capacity')
    # warranty_id = fields.Many2one('product.warranty', string="Product Warranty")
    # solarsystem_id = fields.Many2one('product.solarsystem', string="Solar System")
    # production_id = fields.Many2one('product.estimated_annual_production', string="Annual Production")
    # accessory1_id = fields.Many2one('product.battery_accessory1', string="Accessory-1")
    # accessory2_id = fields.Many2one('product.battery_accessory2', string="Accessory-2")
    # installation_price_id = fields.Many2one('product.installation_price', string="Installation Price")


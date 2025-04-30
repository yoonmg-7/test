from odoo import models,fields

class ProductBatteryAccessory1(models.Model):
    _name = "product.battery.accessory1"
    _description = "Battery Accessory 1"
    _table = "product_battery_accessory1"

    name = fields.Char(string='name', required=True)

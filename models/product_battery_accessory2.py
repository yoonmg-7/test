from odoo import models,fields

class ProductBatteryAccessory2(models.Model):
    _name = "product.battery.accessory2"
    _description = "Battery Accessory 2"
    _table = "product_battery_accessory2"

    name = fields.Char(string="name", required = True)
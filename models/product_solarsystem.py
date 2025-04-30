from odoo import models,fields

class ProductSolarSystem(models.Model):
    _name = "product.solarsystem"
    _description = "Solar System"
    _table = "solar_system"

    name = fields.Char(string="name", required = True)
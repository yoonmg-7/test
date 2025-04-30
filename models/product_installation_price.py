from odoo import models,fields

class ProductInstallationPrice(models.Model):
    _name = "product.installation.price"
    _description = "Installation Price"
    _table = "installation_price"

    name   = fields.Char(string="name", required = True)
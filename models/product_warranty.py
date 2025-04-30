from odoo import models,fields

class ProductWarranty(models.Model):
    _name = "product.warranty"
    _description = "Warranty "
    _table = "warranty"

    warranty_id = fields.Integer
    name = fields.Char(string='name', required=True)

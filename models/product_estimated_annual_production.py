from odoo import models,fields

class ProductEstimatedAnnualProduction(models.Model):
    _name = "product.estimated.annual.production"
    _description = "Estimated Annual Production"
    _table = "estimated_annual_production"

    name = fields.Char(string="name", required = True)

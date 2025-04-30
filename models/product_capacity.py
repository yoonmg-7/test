from odoo import models,fields

class ProductCapacity(models.Model):
    _name = "product.capacity"
    _description = "Capacity"

    name = fields.Char(string="name", required = True)


    # active = fields.Boolean(default=True)
    # #
    # def unlink(self):
    #     for capacity in self:
    #         products = self.env['product.template'].search([('capacity_id', '=', capacity.id)])
    #         products.write({'capacity_id': False})
    #     return super().unlink()
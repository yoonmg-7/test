from odoo import models, fields

class SaleReport(models.Model):
    _inherit = 'sale.report'

    capacity_id = fields.Many2one('product.capacity', string='Capacity')
    warranty_id = fields.Many2one('product.warranty', string="Warranty")
    solarsystem_id = fields.Many2one('product.solarsystem', string="Solar System")
    production_id = fields.Many2one('product.estimated.annual.production', string="Annual Production")
    accessory1_id = fields.Many2one('product.battery.accessory1', string="Accessory-1")
    accessory2_id = fields.Many2one('product.battery.accessory2', string="Accessory-2")
    installation_price_id = fields.Many2one('product.installation.price', string="Installation Price")

    def _select_sale(self):
        select_ = super()._select_sale()
        return select_ + """,
            t.capacity_id,
            t.warranty_id,
            t.solarsystem_id,
            t.production_id,
            t.accessory1_id,
            t.accessory2_id,
            t.installation_price_id
        """

    # def _from_sale(self):
    #     return super()._from_sale() + """
    #         LEFT JOIN product_template pt ON pt.id = l.product_id
    #     """

    def _group_by_sale(self):
        group_by = super()._group_by_sale()
        return group_by + """,
            t.capacity_id,
            t.warranty_id,
            t.solarsystem_id,
            t.production_id,
            t.accessory1_id,
            t.accessory2_id,
            t.installation_price_id
        """
















    # def _select_sale(self):
    #     select_ = super()._select_sale()
    #     return select_ + ', t.capacity_id'
    #
    # def _from_sale(self):
    #     return super()._from_sale() + """
    #                LEFT JOIN product_template pt ON pt.id = l.product_id
    #                LEFT JOIN product_capacity pc ON pc.id = pt.capacity_id
    #            """
    #
    # def _group_by_sale(self):
    #     group_by = super()._group_by_sale()
    #     return group_by + ', t.capacity_id'

from odoo import models, fields,api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    capacity_id = fields.Many2one('product.capacity', string="Capacity")
    warranty_id = fields.Many2one('product.warranty', string="Warranty")
    solarsystem_id = fields.Many2one('product.solarsystem', string="Solar System")
    production_id = fields.Many2one('product.estimated.annual.production', string="Annual Production")
    accessory1_id = fields.Many2one('product.battery.accessory1', string="Accessory-1")
    accessory2_id = fields.Many2one('product.battery.accessory2', string="Accessory-2")
    installation_price_id = fields.Many2one('product.installation.price', string="Installation Price")

    # warranty_id = fields.Many2one('product.warranty', string="Warranty")















    # # department = fields.Many2one( 'hr.department',string="Department")
    # department_id = fields.Many2one('hr.department',
    #                                 string="Department",
    #                                 compute= "_compute_department",
    #                                 store = True,
    #                                 readonly= False)
    #
    # @api.depends('user_id','user_id.department_id')
    # def _compute_department(self):
    #     for record in self:
    #         if record.user_id and record.user_id.department_id:
    #             # Set dep_id1 to the user's department
    #             record.department_id = record.user_id.department_id
    #         else:
    #             # Clear dep_id1 if there's no department
    #             record.department_id = True
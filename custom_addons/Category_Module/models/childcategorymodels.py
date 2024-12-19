from odoo import models, fields
class Childcategory(models.Model):
    _name = 'mymodule.childcategory'
    _description = 'Childcategory'

    name = fields.Char(string='Name', required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='active')
    # subcategory_id = fields.Many2one('mymodule.subcategory', string='Subcategory', domain=[('status','=','active')], required=True)
    category_id = fields.Many2one('mymodule.category', string='Category', domain=[('status', '=', 'active')],required=True)
    subcategory_id = fields.Many2one('mymodule.subcategory', string='Subcategory', domain="[('category_id', '=', category_id),('status', '=', 'active')]",required=True)
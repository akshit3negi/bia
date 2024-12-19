from odoo import models, fields
class Subcategory(models.Model):
    _name = 'mymodule.subcategory'
    _description = 'Subcategory'

    name = fields.Char(string='Name', required=True)
    # active = fields.Boolean(string='Active', default=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='active')
    category_id = fields.Many2one('mymodule.category', string='Category', domain=[('status','=','active')], required=True)
    # childcategory_ids = fields.One2many('mymodule.childcategory', 'subcategory_id', string='Childcategories')
    
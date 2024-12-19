from odoo import models, fields

class Category(models.Model):
    _name = 'mymodule.category'
    _description = 'Category'

    name = fields.Char(string='Name', required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='active')
    subcategory_ids = fields.One2many('mymodule.subcategory', 'category_id', string='Subcategories')
    # childcategory_ids=fields.One2many('mymodule.childcategory', 'category_id', string='Childcategories')
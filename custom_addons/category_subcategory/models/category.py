from odoo import models, fields

class Category(models.Model):
    _name = 'category.model'
    _description = 'Category'

    name = fields.Char(string='Category Name', required=True)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string="Status")

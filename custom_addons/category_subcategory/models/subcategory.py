from odoo import models, fields

class Subcategory(models.Model):
    _name = 'subcategory.model'
    _description = 'Subcategory'

    name = fields.Char(string='Subcategory Name', required=True)
    category_id = fields.Many2one('category.model', string='Category', domain= [('status','=','active')],  required=True)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string="Status")

from odoo import models, fields

class Childcategory(models.Model):
    _name = 'childcategory.model'
    _description = 'Childcategory'

    name = fields.Char(string='Childcategory Name', required=True)
    category_id = fields.Many2one('category.model', string='Category', domain= [('status','=','active')],  required=True)
    subcategory_id = fields.Many2one('subcategory.model', string='Subategory', domain= [('status','=','active')],  required=True)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string="Status")

from odoo import models, fields,api

class Employee(models.Model):
    _inherit = "crm.lead"
    

    sub_status = fields.Many2one('bradford.substatus', string="Sub Status")
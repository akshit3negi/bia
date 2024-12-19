from odoo import models, fields


class mainstatus(models.Model):
    _name = "main.status"
    _description = "Main status fields"

    name = fields.Char(string="Main-Status", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")
   
    substatus_var = fields.One2many(
        "sub.status", "mainstatus_var", string="Sub-Status"
    )
   
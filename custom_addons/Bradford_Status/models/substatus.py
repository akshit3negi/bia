from odoo import models, fields

class Substatus(models.Model):
    _name = "sub.status"
    _description = "Sub status fields"

    name = fields.Char(string="Sub-Status", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")
    mainstatus_var = fields.Many2one("main.status", string="Main Status",
        domain=[("state", "=", "active")],
        required=True)

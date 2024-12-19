from odoo import models, fields

class University(models.Model):
    _name = "bradford.university"
    _description = "University"

    name = fields.Char(string="University", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")

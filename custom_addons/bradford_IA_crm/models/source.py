from odoo import models, fields

class Source(models.Model):
    _name = "bradford.source"
    _description = "Source"

    name = fields.Char(string="Source", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")

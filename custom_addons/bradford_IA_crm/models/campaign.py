from odoo import models, fields

class campaign(models.Model):
    _name = "bradford.campaign"
    _description = "Campaign"

    name = fields.Char(string="Campaign", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")
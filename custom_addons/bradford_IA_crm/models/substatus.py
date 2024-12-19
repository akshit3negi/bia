from odoo import models, fields


class Substatus(models.Model):
    _name = "bradford.substatus"
    _description = "Sub status of lead"

    name = fields.Char(string="Sub-Status", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State",
        default="active",
    )
    lead_status = fields.Many2one(
        "crm.stage",
        string="Lead Status",
        required=True,
    )

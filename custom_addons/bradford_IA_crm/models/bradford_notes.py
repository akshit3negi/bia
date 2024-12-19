from odoo import models, fields
from datetime import datetime

class notes(models.Model):
    _name = "bradford.notes"
    _description = "Notes"

    name = fields.Char(string="Subject", required=True)
    contact = fields.Many2one('crm.lead',string="Contact", help="CRM Leads")
    relatedto = fields.Selection(
        [("lead", "Lead"), ("emial", "Email")],
        string="Related To", default="Lead")
    
    attach=fields.Binary(string="Attachment")
    note=fields.Text(string="Note",)
    assignedto=fields.Many2one('res.partner', string="Assigned To", default="admin")
    createdby=fields.Char(string="Created by", required=True)

    exit = fields.Datetime(string='Date Current Action',default=datetime.now())
   
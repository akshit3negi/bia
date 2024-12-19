from odoo import models, fields, api


class task(models.Model):
    _name = "bradford.task"
    _description = "Tasks module"

    name = fields.Char(string="Subject", required=True)
    status = fields.Selection(
        [
            ("notstarted", "Not Started"),
            ("inprogress", "InProgress"),
            ("completed", "Completed"),
            ("pendinginput", "Pending Input"),
            ("deferred", "Deferred"),
        ],
        string="Status",
        default="notstarted",
        required=True,
    )  # group_expand="_get_status_groups",

    relatedto = fields.Selection(
        [
            ("account", "Account"),
            ("contact", "Contact"),
            ("task", "Task"),
            ("opportunity", "Opportunity"),
            ("bug", "Bug"),
            ("case", "Case"),
            ("lead", "Lead"),
            ("project", "Project"),
            ("projecttask", "Project Task"),
            ("target", "Target"),
            ("contract", "Contract"),
            ("invoice", "Invoice"),
            ("quote", "Quote"),
            ("product", "Product"),
        ],
        string="Related To:",
        default="task",
        required=True,
    )

    startdate = fields.Datetime(string="Start Date & Time")
    duedate = fields.Datetime(string="Due Date & Time")
    
    
    
    contact = fields.Many2one("res.partner", string="Contact Name")
    priority = fields.Selection(
        [("0", "Low"), ("1", "Normal"),("2", "Medium"), ("3", "High")],
        string="Priority",
        dfault="0",
    )

    descrip = fields.Text(string="Description")

    assignedto = fields.Many2one("res.users", string="Assigned to")

    createdon = fields.Datetime(
        string="Created On", default=fields.Datetime.now(), readonly=1
    )
    
    

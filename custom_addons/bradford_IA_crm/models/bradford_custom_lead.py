from odoo import models, fields
 
class Lead(models.Model):
    _inherit = 'res.partner'  
    
    date = fields.Date(string="Date")
 
    country_code = fields.Char(string="Country Code")
    phone_number = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")
 
 
    job_title=fields.Many2one('bradford.jobtitle',string="Job Title")
    source = fields.Many2one('bradford.source', string="Lead Source", required=True)
    assigned_to = fields.Many2one('res.users', string="Assigned To",help="Select the salesperson to assign this lead to")
    highest_qualification = fields.Many2one('bradford.highestqualification',string="Highest Qualification")
    work_experience = fields.Many2one('bradford.workexperience',string="Work Experience (in years)")
    program = fields.Many2one('bradford.programinterested', string="Program Interested")
    campaign = fields.Many2one('bradford.campaign',string="Campaign Name")
 
    university= fields.Many2one('bradford.university',string="University")
    courses = fields.Many2one('bradford.courses',string="Courses")
 
    lead_status = fields.Many2one(
        'crm.stage',
        string="Lead Status",required=True)
    sub_status = fields.Many2one('bradford.substatus', string="Sub Status", domain="[('lead_status','=', lead_status), ('state','=','active')]")
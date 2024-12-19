from odoo import fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient records"

    name = fields.Char(string='Name', required= True)
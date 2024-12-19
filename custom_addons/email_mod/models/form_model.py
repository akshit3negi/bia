from odoo import models, fields, api

class FormConfirmation(models.Model):
    _name = 'form.confirmation'
    _description = 'Form Confirmation'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    dob = fields.Date(string='Date of Birth')

    @api.model
    def create(self, vals):
        record = super(FormConfirmation, self).create(vals)
        record.send_confirmation_email()
        return record

    def send_confirmation_email(self):
        template = self.env.ref('email_mod.email_template_confirmation')  # Adjust if necessary
        if template:
            template.send_mail(self.id, force_send=True)
        else:
            raise ValueError("Email template not found.")


    @api.model
    def action_submit(self):
    # Create a new record in the form.confirmation model using the current record's data
        self.create({
        'name': self.name,
        'email': self.email,
        'phone_number': self.phone_number,
        'gender': self.gender,
        'date_of_birth': self.date_of_birth,
        })
    
    # Optionally, send a confirmation email (you should have an email template defined)
        self.send_confirmation_email()

    # Return a success notification to the user
        return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': 'Success',
            'message': 'Your submission has been received!',
            'sticky': False,
        },
    }
        
        
from odoo import fields, models, api
from odoo.exceptions import UserError

class FormRegistration(models.Model):
    _name = "registration.form"
    _description = "Employee records"

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    address = fields.Text(string='Address', required=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Password', required=True)

    # def action_send_email(self):
    #     # Ensure that an email address is provided
    #     if not self.email:
    #         raise UserError("Please provide an email address.")
    #     # Compose and send email
    #     mail_template = self.env.ref('Form.email_template_registration_form')
    #     if mail_template:
    #         mail_template.send_mail(self.id, force_send=True)

    # def action_send_email(self):
    #     if not self.email:
    #         raise UserError("Please provide an email address.")
    #     # Compose and send email
    #     mail_template = self.env.ref('Form.email_template_registration_form')
    #     if mail_template:
    #         # Render the template for debugging
    #         rendered_body = mail_template._render_template(mail_template.body_html, 'registration.form', [self.id])
    #         # Ensure the context is passed correctly
    #         mail_template.with_context(lang=self.env.user.lang).send_mail(self.id, force_send=True)
            
    def action_send_email(self):
        template = self.env.ref("Form.email_template_registration_form")
        if not template:
            raise UserError("Email template not found. Please define it.")
        for record in self:
            email = record.email
            if not email:
                raise UserError("No valid email address found for reminders.")
            email_values = template.generate_email(record.id, fields=["body_html"])
            body_html = (
                email_values["body_html"]
                .replace("${object.name}", record.name or "...")
                .replace("${object.gender}", record.gender or "...")
                .replace("${object.address}", record.address or "...")
                .replace("${object.email}", record.email or "...")
            )            
            email_value = template.generate_email(record.id, fields=["subject"])
            subject = (
                email_value["subject"]
                .replace("${object.name}", record.name or "...")
            )            
            mail_values = {
                "email_to": email,
                "subject": subject,
                "body_html": body_html,
            }
            mail = self.env["mail.mail"].create(mail_values)
            mail.send()
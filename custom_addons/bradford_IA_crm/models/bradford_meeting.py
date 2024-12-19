from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import format_datetime
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class meet(models.Model):
    # _inherit="event.event"
    _name = "bradford.meet"
    _description = "Meeting module"

    name = fields.Char(string="Subject", required=True)
    stage = fields.Selection(
        [("planned", "Planned"), ("held", "Held"), ("notheld", "Not Held")],
        string="Status",
        group_expand="_get_status_groups",
        default="planned",
        required=True,
    )
    relatedto = fields.Many2one("res.partner", string="Related to")
    venue = fields.Char(string="Venue")

    startdate = fields.Datetime(string="Start Date & Time")
    enddate = fields.Datetime(string="End Date & Time")
    duration = fields.Char(string="Duration", compute="_compute_duration", store=True)

    descrip = fields.Text(string="Description")
    assignedto = fields.Many2one("res.partner", string="Assigned to")

    reminduser = fields.Many2many(
        "res.partner", string="Reminders", help="Customers to remind for this activity."
    )
    
    hrbefore=fields.Integer(string="Send before(in hr.)")
    
    createdon = fields.Datetime(
        string="Created On", default=fields.Datetime.now(), readonly=1
    )

    color = fields.Integer(String="Kanban Card Color")

    cancelled = fields.Boolean(string="Cancelled")


# ----->>>>> meeting can't be held when the current time is between start and end time <<<<<-----
    @api.onchange("stage")
    def onchange_stage(self):
        if self.stage == "held":
            self.ensure_stage_not_held_during_meeting()
    def ensure_stage_not_held_during_meeting(self):
        """Ensure that the meeting stage cannot be 'held' if the current time is between startdate and enddate."""
        current_time = fields.Datetime.now()
        for record in self:
            if record.stage == "held" and record.startdate and record.enddate:
                if record.startdate <= current_time <= record.enddate:
                    raise ValidationError(
                        "The meeting stage cannot be set to 'Held' while it is in progress. \n Start time <= Current time <= End time"
                    )

    # ----->>>>> For Not Held meetings <<<<<------
    @api.onchange("cancelled")
    def _onchange_cancelled(self):
        if self.cancelled:
            self.stage = "notheld"
    @api.onchange("stage")
    def _onchange_stage(self):
        if self.stage != "notheld":
            self.cancelled = False

    # ------>>>>> Stage: Planned to Held when current time extends end time <<<<<-----
    def action_update_meeting_status(self):
        """Update meeting state from Planned to Held based on enddate."""
        current_time = fields.Datetime.now()
        meetings_to_update = self.search(
            [("stage", "=", "planned"), ("enddate", "<=", current_time)]
        )
        for meeting in meetings_to_update:
            meeting.stage = "held"
            
            
    # ------>>>>> Stage: Held to Planned when End time > Current time. <<<<<-----
    def action_update_meeting_status2(self):
        """Update meeting state from Held to Planned based on enddate."""
        current_time = fields.Datetime.now()
        stage_to_update = self.search(
            [("stage", "!=", "planned"), ("enddate", ">", current_time)]
        )
        for meeting in stage_to_update:
            meeting.stage = "planned"

    # ----->>>>> Order the stages in Kanban view <<<<<-----
    @api.model
    def _get_status_groups(self, *args, **kwargs):
        # Return the statuses in the desired order
        return ["planned", "held", "notheld"]

    # ----->>>>> for endate>startdate <<<<<-----
    @api.constrains("startdate", "enddate")
    def _check_date_range(self):
        for record in self:
            # Check if startdate and enddate are set
            if record.startdate and record.enddate:
                if record.enddate <= record.startdate:
                    raise ValidationError(
                        "End Date & Time must be after the Start Date & Time."
                    )

    # ----->>>>> for Duration calculation <<<<<-----
    @api.depends("startdate", "enddate")
    def _compute_duration(self):
        for record in self:
            if (record.startdate and record.enddate) and (
                record.enddate > record.startdate
            ):
                # Calculate the time difference
                delta = record.enddate - record.startdate
                # Get total seconds from timedelta
                total_seconds = delta.total_seconds()

                # Calculate the number of days
                days = int(total_seconds // 86400)  # 86400 seconds in a day

                # Calculate the remaining hours
                hours = int((total_seconds % 86400) // 3600)  # 3600 seconds in an hour

                # Calculate the remaining minutes
                minutes = int((total_seconds % 3600) // 60)  # 60 seconds in a minute

                # Format the duration as "X days Y hours Z minutes"
                record.duration = f"{days} day {hours} hr {minutes} min"
            else:
                record.duration = "N/A"

    # ----->>>>> to extract emails from the customer tags field <<<<<-----
    def get_reminder_emails(self):
        """Extract emails of all reminder partners."""
        for record in self:
            # Extract emails of all linked partners
            emails = record.reminduser.mapped("email")
            # Filter out any empty or invalid email addresses
            emails = [email for email in emails if email]
            return emails

    # --->>> to show the extracted email from the customer tags field on a popup <<<---
    # def action_show_emails(self):
    #     """Action to display emails in a notification."""
    #     for record in self:
    #         emails = record.get_reminder_emails()
    #         message = ", ".join(emails) if emails else "No emails found for reminders."
    #         return {
    #             'type': 'ir.actions.client',
    #             'tag': 'display_notification',
    #             'params': {
    #                 'title': 'Reminder Emails',
    #                 'message': message,
    #                 'type': 'info',  # Can be 'info', 'warning', or 'danger'
    #                 'sticky': False,  # If True, the notification stays on screen
    #             },
    #         }

    # ----->>>>> email triggered, but time zone issue <<<<<------
    # def action_send_invitations(self):
    #     """Send invitation emails to reminder partners."""
    #     # Fetch the email template
    #     template = self.env.ref('bradford_IA_crm.email_template_invitation')
    #     if not template:
    #         raise UserError("Email template not found. Please define it.")

    #     for record in self:
    #         # Get emails from the reminder partners
    #         emails = record.get_reminder_emails()

    #         if not emails:
    #             raise UserError("No valid email addresses found for reminders.")

    #         # Send email to each extracted email
    #         for email in emails:

    #             # # Ensure that the email template is used properly for external email
    #             # mail_values = {
    #             #     'email_to': email,
    #             #     'body_html': template.body_html,
    #             #     'subject': template.subject,
    #             # }

    #             # # Create and send the email
    #             # mail = self.env['mail.mail'].create(mail_values)
    #             # mail.send()

    #             template.write({'email_to': email})  # Set the email_to field
    #             template.send_mail(record.id, force_send=True)

    #         # Restore the template's original email_to (if needed)
    #         template.write({'email_to': False})

    # ---->>>> Final function to send a scheduled mail, 1hr before the start time <<<<----
    def action_send_invitations(self):
        template = self.env.ref("bradford_IA_crm.email_template_invitation")
        if not template:
            raise UserError("Email template not found. Please define it.")
        for record in self:
            emails = record.get_reminder_emails()
            if not emails:
                raise UserError("No valid email addresses found for reminders.")

            # Convert startdate and enddate to the user's time zone
            user_tz = self.env.user.tz or "UTC"
            startdate_local = format_datetime(self.env, record.startdate, tz=user_tz)
            enddate_local = format_datetime(self.env, record.enddate, tz=user_tz)

            # Generate the email content using the template
            email_values = template.generate_email(record.id, fields=["body_html"])
            body_html = (
                email_values["body_html"]
                .replace("${startdate_local}", startdate_local)
                .replace("${enddate_local}", enddate_local)
                .replace("${object.name}", record.name or "...")
                .replace("${object.venue}", record.venue or "...")
                .replace("${object.duration}", record.duration or "...")
                .replace("${object.descrip}", record.descrip or "...")
            )

            # -->> For Scheduling <<--
            hr = int(record.hrbefore) if record.hrbefore else 0
            scheduled_time = record.startdate - timedelta(hours=hr)

            for email in emails:
                mail_values = {
                    "email_to": email,
                    "subject": template.subject,
                    "body_html": body_html,
                    "scheduled_date": scheduled_time,
                }
                mail = self.env["mail.mail"].create(mail_values)
                # mail.send()

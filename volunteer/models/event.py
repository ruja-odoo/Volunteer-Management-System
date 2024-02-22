from odoo import fields, models

class event(models.Model):
    _name = "volunteer.event"
    _description = "Events containing opportunities for volunteering"

    title = fields.Char(required=True, string="Title")
    description = fields.Text()
    date=fields.Date()

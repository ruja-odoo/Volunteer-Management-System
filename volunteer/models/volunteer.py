from odoo import fields, models


class volunteer(models.Model):
    _name = "volunteer.volunteer"
    _description = "Volunteer"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, string="Name")
    id = fields.Integer("id", required=True)
    mobile = fields.Char(string="Mobile")
    skills = fields.Selection(
        string="Skills",
        selection=[
            ("comm", "Communication"),
            ("evPlan", "Event Planning"),
            ("mark", "Marketing"),
            ("custServ", "Customer Service"),
            ("social", "Social Media"),
        ],
        required=True,
        copy=False,
    )

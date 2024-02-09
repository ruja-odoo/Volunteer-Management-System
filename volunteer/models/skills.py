from odoo import fields, models

class skill(models.Model):
    _name = "volunteer.skill"
    _description = "Skills"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    skill = fields.Char(required=True, string="Title")
    id = fields.Integer("id", required=True)
    description = fields.Text()

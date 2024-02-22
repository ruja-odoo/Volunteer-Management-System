from odoo import fields, models

class skill(models.Model):
    _name = "volunteer.skill"
    _description = "Skills"

    skill = fields.Char(required=True, string="Title")
    id = fields.Integer("id", required=True)
    description = fields.Text()

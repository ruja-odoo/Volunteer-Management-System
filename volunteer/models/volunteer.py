from odoo import fields, models


class volunteer(models.Model):
    _name = "volunteer.volunteer"
    _description = "Volunteer"

    name = fields.Char(required=True, string="Name")
    mobile = fields.Char(string="Mobile")
    skills = fields.Many2many("volunteer.skill" , string= "Skills")

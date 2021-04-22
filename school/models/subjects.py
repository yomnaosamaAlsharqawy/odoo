from odoo import models, fields, api
class SchoolSubjects(models.Model):
    _name = 'school.subjects'
    _description = 'Class subject'

    # fields

    subject = fields.Char()
    teacher_id = fields.Many2one('res.partner')
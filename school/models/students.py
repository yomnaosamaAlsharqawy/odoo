from odoo import models, fields, api


class SchoolStudents(models.Model):
    _name = 'school.students'
    _description = 'Class Student'

    # fields

    name = fields.Char()
    Birthday = fields.Date()
    address = fields.Char()
    email = fields.Char()
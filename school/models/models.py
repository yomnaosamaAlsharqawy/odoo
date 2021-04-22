from odoo import models, fields, api

class SchoolSystem(models.Model):
    _name = 'school.systems'
    _description = 'Class system'

    # fields

    subject_id = fields.Many2one('school.subjects')
    grade = fields.Float()
    year = fields.Date()
    student_id = fields.Many2one('school.students')











# class school(models.Model):
#     _name = 'school.school'
#     _description = 'school.school'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

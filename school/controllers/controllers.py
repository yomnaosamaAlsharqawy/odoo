# -*- coding: utf-8 -*-
from odoo import http
import json
import requests


class School(http.Controller):
    # students endpoints 
    @http.route('/school/student/list', auth='public', methods=['GET'])
    def student_list(self):
        student_objs = http.request.env['school.students'].sudo().search([])
        student_list=[]
        for i in student_objs:
            student = {'name':i.name, 'address':i.address, 'birthday':str(i.Birthday), 'email':i.email}
            # print(i.Birthday)
            student_list.append(student)
        return json.dumps(student_list)
    

    @http.route('/school/student/create', auth='public', methods=['POST'], csrf=False)
    def student_create(self, *args, **kwargs):
        if kwargs:
            student_obj = http.request.env['school.students'].sudo().create(kwargs)
            result = {'status':200, 'student_name':student_obj.name}
        else:
            result = {'status':404, 'error':'there is now data to create student'}

        return json.dumps(result)

    

    

    @http.route('/school/subjects/list', auth='public', methods=['GET'])
    def subject_list(self):
        subject_objs = http.request.env['school.subjects'].sudo().search([])
        subject_list=[]
        for i in subject_objs:
            subject = {'subject':i.subject, 'teacher':i.teacher_id.name}
            
            subject_list.append(subject)
        return json.dumps(subject_list)


    @http.route('/school/subjects/create', auth='public', methods=['POST'], csrf=False)
    def student_create(self, *args, **kwargs):
        if kwargs:
            teacher = http.request.env['res.partner'].sudo().search(
            [('name', '=', kwargs.get('teacher_id'))])

            kwargs['teacher_id'] = teacher.id
            subject_obj = http.request.env['school.subjects'].sudo().create(kwargs)
            result = {'status':200, 'subjects_name':subject_obj.subject}
        else:
            result = {'status':404, 'error':'there is now data to create student'}

        return json.dumps(result)



class SchoolSystem(http.Controller):
    
    # school system end points ************************

    # select all student in specific subject
    @http.route('/school/school/list', auth='public', methods=['GET'])
    def student(self, *args, **kwargs):
        subject = http.request.env['school.subjects'].sudo().search(
            [('subject', '=', kwargs.get('subject_id'))])

        kwargs['subject_id'] = subject.id
        subject_objs = http.request.env['school.systems'].sudo().search([('subject_id', '=', kwargs.get('subject_id'))])
        subject_list=[]
        for i in subject_objs:
            subject = {'student':i.student_id.name, 'subject':i.subject_id.subject, 'year':str(i.year), 'grade':i.grade}
            
            subject_list.append(subject)
        return json.dumps(subject_list)

    # select all subject of specific student
    @http.route('/school/school/student/list', auth='public', methods=['GET'])
    def subject(self, *args, **kwargs):
        student = http.request.env['school.students'].sudo().search(
            [('name', '=', kwargs.get('student_id'))])

        kwargs['student_id'] = student.id
        subject_objs = http.request.env['school.systems'].sudo().search([('student_id', '=', kwargs.get('student_id'))])
        subject_list=[]
        for i in subject_objs:
            subject = {'student':i.student_id.name, 'subject':i.subject_id.subject, 'year':str(i.year), 'grade':i.grade}
            
            subject_list.append(subject)
        return json.dumps(subject_list)

    # create new record in school system
    @http.route('/school/system/create', auth='public', methods=['POST'], csrf=False)
    def system_create(self, *args, **kwargs):
        if kwargs:
            # select from subject model
            subject = http.request.env['school.subjects'].sudo().search(
            [('subject', '=', kwargs.get('subject_id'))])

            kwargs['subject_id'] = subject.id

            # select from student model
            student = http.request.env['school.students'].sudo().search(
            [('name', '=', kwargs.get('student_id'))])

            kwargs['student_id'] = student.id
            system_obj = http.request.env['school.systems'].sudo().create(kwargs)
            result = {'status':200, 'message':'created successfuly'}
        else:
            result = {'status':404, 'error':'there is now data to create student'}

        return json.dumps(result) 






    # update record in school system
    @http.route('/school/system/update', auth='public', methods=['POST'], csrf=False)
    def system_update(self, *args, **kwargs):
        if kwargs:
            # select from subject model
            subject = http.request.env['school.subjects'].sudo().search(
            [('subject', '=', kwargs.get('subject_id'))])

            kwargs['subject_id'] = subject.id

            # select from student model
            student = http.request.env['school.students'].sudo().search(
            [('name', '=', kwargs.get('student_id'))])

            kwargs['student_id'] = student.id
            system_obj = http.request.env['school.systems'].sudo().search(
            [('subject_id', '=', kwargs.get('subject_id')), ('student_id', '=', kwargs.get('student_id'))])
            system_obj.write({'grade':kwargs.get('grade')})
            result = {'status':200, 'student':system_obj.student_id.name, 'grade':system_obj.grade}
        else:
            result = {'status':404, 'error':'there is now data to create student'}

        return json.dumps(result)


    # delete from school system
    @http.route('/school/system/delete', auth='public', methods=['POST'], csrf=False)
    def system_delete(self, *args, **kwargs):
        if kwargs:
            system_obj = http.request.env['school.systems'].sudo().search([('id', '=', kwargs.get('id'))])
            system_obj.unlink()
            result = {'status':200, 'message':'deleted successfuly'}
        else:
            result = {'status':404, 'error':'there is now data to create student'}

        return json.dumps(result)

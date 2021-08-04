# -*- coding: utf-8 -*-

import json
from odoo import http
from odoo.http import request


class Homepage(http.Controller):
    @http.route('/hastane', auth='public', website=True)
    def main_page(self):
        return request.render('hastane.main_page')


class AddedRecord(http.Controller):
    @http.route('/created', auth='user', website=True)
    def created(self):
        return request.render('hastane.thanks')


class GetDoctors(http.Controller):
    @http.route('/doctors', auth='user', website=True)
    def get_doctors(self):
        doctors = request.env['doctor.doctor'].sudo().search([])
        val = {
            'doctors': doctors
        }
        return request.render('hastane.get_doctors', val)

class GetHospitals(http.Controller):
    @http.route('/hospitals', auth='user', website=True)
    def get_hospitals(self):
        hospitals = request.env['hospital.hospital'].sudo().search([])
        val = {
            'hospitals': hospitals
        }
        return  request.render('hastane.get_hospitals', val)

class GetPatients(http.Controller):
    @http.route('/patients', auth='user', website=True)
    def get_patients(self):
        patients = request.env['patient.patient'].sudo().search([])
        val = {
            'patients': patients
        }
        return request.render('hastane.get_patients', val)

class Patient(http.Controller):
    @http.route('/new_create/hasta', auth='user', website=True)
    def hasta_kayit(self, **kw):
        doctors = request.env['doctor.doctor'].sudo().search([])
        return request.render('hastane.hasta_kayit', {
            'doctors': doctors
        })

    @http.route('/created/hasta', auth='user', website=True)
    def added_hst(self, **kw):
        val = {
            'name': kw.get('name'),
            'hospital_id': kw.get('hospital_id'),
            'doctor_ids': [(0, 0, kw.get('doctor_ids'))]
        }

        request.env['patient.patient'].create(val)

        return request.redirect('/')


class Doctor(http.Controller):
    @http.route('/new_create/doctor', auth='user', website=True, csrf=True)
    def doctor_kayit(self):
        hospitals = request.env['hospital.hospital'].sudo().search([])
        type_of_degrees = request.env['type.of.degrees'].sudo().search([])
        val = {
            'hospitals': hospitals,
            'type_of_degrees': type_of_degrees
        }
        return request.render('hastane.doctor_kayit', val)
        # python.exe .\odoo-bin -c .\odoo.conf

    @http.route('/created/doctor', auth='user', website=True)
    def doctor_add(self, **kw):
        data = {
            'name': kw.get('name'),
            'hospital_ids': [(6, 0, [int(kw.get('hospital_id'))])],
            'age': kw.get('age'),
            'type_of_degree': kw.get('type_of_degree'),
            'graduated_school': kw.get('graduated_school')
        }
        request.env['doctor.doctor'].sudo().create(data)
        return request.redirect('/created')

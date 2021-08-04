from odoo import models, fields, api
from datetime import date


class Patient(models.Model):
    _name = 'patient.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patients'

    name = fields.Char('name',
                       required=True)
    hospital_id = fields.Many2one('hospital.hospital', string='İlgili hastane')
    doctor_ids = fields.Many2many('doctor.doctor', 'patient_doctor_rel', 'patient_id', 'doctor_id')


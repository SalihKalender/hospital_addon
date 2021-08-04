from odoo import models, fields, api


class Hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'hospital.hospital'

    name = fields.Char('hospital_adi',required=True)
    released_date = fields.Date('Kurulus _yili',required=True)
    description = fields.Text('aciklama')
    #? patient_ids = fields.One2many('patient.patient','hospital_id')  #-- patient'lerin hospital_id'sine bunu verecek
    #-- Yukarıdaki patient_ids'i silince patients bolumu gitti,


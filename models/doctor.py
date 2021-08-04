from odoo import models, fields, api


class Doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'Hastanedeki doktorlar'

    sequence = fields.Integer()
    name = fields.Char('name')
    hospital_ids = fields.Many2many('hospital.hospital', 'hospital_doctor_rel', 'hospital_id', 'doctor_id')
    # -- 1 , rel , 1 , 2
    age = fields.Integer('Yas')
    graduated_school = fields.Char('Mezun Oldugu Okul')
    type_of_degree = fields.Many2one('type.of.degrees', string='Type of Degree')
    active = fields.Boolean(default=True)

    @api.model
    def doktor_zeka_hesapla(self, a):
        return a * 2

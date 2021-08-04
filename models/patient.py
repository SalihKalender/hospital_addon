from odoo import models, fields, api
from datetime import date


class Patient(models.Model):
    _name = 'patient.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patients'

    name = fields.Char('name',
                       required=True)  # -- string='' parametresi default value atar ILK PARAMETREDE KULLANACAKSAN
    # kayit_tarihi = fields.Date('Kayit tarihi')    #-- default eklemeyi arastır
    hospital_id = fields.Many2one('hospital.hospital', string='İlgili hastane')  # -- class adimi db adimi arastir
    doctor_ids = fields.Many2many('doctor.doctor', 'patient_doctor_rel', 'patient_id', 'doctor_id')

    def action_test(self):
        pass
        # val = {
        #     'name': 'Örnek Doktor',
        #     'hospital_ids': [(0, 0, {
        #         'name': 'Örnek hastane',
        #         'released_date': fields.Date.today()
        #     })]
        # }
        #
        # doctor = self.env['doctor.doctor'].create(val)
        # doctor = self.env['doctor.doctor'].browse(doctor.id)
        #
        # bulunan = self.env['doctor.doctor'].sudo().search([
        #     ('name', 'like', '%ismail%')
        # ], limit=1)
        #
        # if doctor:
        #     doctor.write({
        #         'name': 'Hasan'
        #     })

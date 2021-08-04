from odoo import api,fields,models

class TypeOfDegrees(models.Model):
    _name = 'type.of.degrees'

    name = fields.Char('name')

# -*- coding: utf-8 -*-
{
    'name': "hastane",

    'summary': """
        Hastane ve hasta randevu isleri
    """,

    'description': """
        Hastanenin database'si, randevuların database'si, alayının database'si
    """,

    'author': "Salih Kalender",
    'website': "http://www.salihkalender.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'website',
        'web',
        'mail'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/type_of_degrees.xml',
        'views/hospital.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/templates.xml',
        'views/patient_web.xml',
        'views/doctor_web.xml',
        'views/thanks.xml',
        'views/hospital_web.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'sequence': 1,
    'license': 'LGPL-3'
}

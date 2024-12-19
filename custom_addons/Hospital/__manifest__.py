{
    'name': 'Hospital Management System',
    'author':'Akshit',
    'version': '1.0',
    'description': "This module based on Hospital management.",
    'depends': ['base'],
    'data': [
         'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
    ],
    'installable': True,
    'application': True,
}

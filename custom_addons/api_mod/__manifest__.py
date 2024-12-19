{
    'name': 'User API',
    'author': 'Akshit',
    'description': 'User API Module',
    'version': '1.0',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'views/menu.xml',
             'views/viewuser.xml'],
    'installable': True,
    'application': True,
}

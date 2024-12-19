{
    'name':'Form',
    'author': 'Arnav',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'views/menu.xml',
        'views/form.xml',
    ],
    'installable': True,
    'application': True,
}
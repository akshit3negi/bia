{
    'name': 'Category',
    'author':'Akshit',
    'version': '1.0',
    'description': "This module allows managing categories, subcategories, and childcategories with active/inactive status.",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/categoryview.xml',
        'views/subcategoryview.xml',
        'views/childcategoryview.xml', 
    ],
    'installable': True,
    'application': True,
}

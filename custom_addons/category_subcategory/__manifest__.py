{
    'name': 'Category match',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Module with Category and Subcategory structure',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/category_views.xml',
        'views/subcategory_views.xml',
        'views/childcategory_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}

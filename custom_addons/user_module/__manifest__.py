{
    "name": "User Module",
    "author": "Akshit",
    "version": "1.0.0",
    "description": "This module allows managing User details",
    "depends": ["base"],
    "assets": {
        "web.assets_backend": [
            "user_module\static\src\css\custom_styles.css",
        ],
    },
    "data": ["security/ir.model.access.csv", "views/menu.xml", "views/userview.xml"],
    "installable": True,
    "application": True,
}

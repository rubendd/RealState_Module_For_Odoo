# -*- coding: utf-8 -*-
{
    "name": "escuela",
    "summary": """
        Practica de Odoo creando el modulo llamado escuela""",
    "description": """
        para mostrar notas de los alumnos
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Recursos Humanos",
    "version": "0.1",
    "installable": True,
    "auto_install": False,
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}

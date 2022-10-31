# -*- coding: utf-8 -*-
{
    'name': "zue_curso_productos",

    'summary': """
        Aplicativo para el curso de ZUE Odoo almacenamiento de productos""",

    'description': """
        Aplicativo para el curso de ZUE Odoo:
            - Almacenamiento de productos
            - Reporte de inventario
            - Documentación de productos
    """,

    'author': "ZUE S.A.S",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/actions_products.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

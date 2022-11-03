# -*- coding: utf-8 -*-
{
    'name': "zue_curso",

    'summary': """
        App para curso de odoo ZUE """,

    'description': """
        App curso zue con el siguente contenido:
            -Modelos
            -Vistas
            -Acciones
            -ORM
            -API
        etc.
    """,

    'author': "ZUE S.A.S",    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/views_transient.xml',
        'views/inherit_views_partner.xml',
        'views/actions_employee.xml',
        'views/menus.xml',
        'views/actions_proveedores.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

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
    'category': 'ZUE Curso',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','mail','calendar','base_address_city'],

    # always loaded
    'data': [
        'security/proveedores_security.xml',
        'security/proveedores_rules.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/actions_proveedores_authorized_wizard.xml',
        'views/views_transient.xml',
        'views/inherit_views_partner.xml',
        'views/actions_employee.xml',
        'views/actions_proveedores.xml',
        'views/actions_proveedores_print_report.xml',
        'reports/template_report_proveedores.xml',
        'reports/actions_report_proveedores.xml',
        'templates/index.xml',
        'views/menus.xml',
        'data/master_data.xml',
        'data/data_city.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

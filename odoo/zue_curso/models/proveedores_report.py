from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

class zue_curso_proveedores_print_report(models.TransientModel):
    _name = 'zue_curso.proveedores_print_report'
    _description = 'Imprimir reporte de proveedores'

    report_id = fields.Many2one('zue_curso.report_proveedores', string='Reporte')

    def print_report(self):
        datas = {
            'id': self.id,
            'model': 'zue_curso.proveedores_print_report'
        }

        return {
            'type':'ir.actions.report',
            'report_name':'zue_curso.report_list_proveedores',
            'report_type':'qweb-pdf',
            'datas':datas
        }

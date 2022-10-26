from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class zue_curso_employee(models.Model):
    _name = 'zue_curso.employee'
    #_inherit = ['res.partner']
    _description = 'Empleados curso'

    name = fields.Char(string='Nombre')
    date_vinculation = fields.Date(string='Fecha de vinculación', required=False)
    wage = fields.Float(string='Salario')
    date_start_company = fields.Date(string='Fecha ingreso compañía')
    channel_ids = fields.Char(string='Canales a ajustar')
    report_ids = fields.Char(string='Reportes a ajustar')



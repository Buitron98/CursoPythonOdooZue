# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class zue_curso_proveedores(models.Model):
    _name = 'zue_curso.proveedores'
    _description = 'Proveedores del curso'
    _order = 'type_proveedor'
    _fold_name = 'type_proveedor'
    #_rec_name = 'complate_name'

    complate_name = fields.Char(string='Nombre', required=True, help='En este campo se digita el nombre del proveedor')
    type_document = fields.Selection([('NIT','NIT'),
                                      ('CC','Cedula de ciudadania'),
                                      ('PA','Pasaporte'),
                                      ('OT','Otro')], string='Tipo de documento', required=True, default='NIT')
    num_document = fields.Char(string='Número de documento', required=True)
    active = fields.Boolean(string='Activo')
    value = fields.Float(string='Valor')
    description = fields.Text(string='Descripción')
    type_proveedor = fields.Selection([('a','Adquiriente'),('b','Prestamista'),('c','Publico')], string='Tipo')
    date_vinculation = fields.Date(string='Fecha de vinculación', required=True)
    partner_id = fields.Many2one('res.partner',string='Contacto asociado',domain="[('parent_id','!=',False)]")
    report_ids = fields.Many2many('zue_curso.report_proveedores', string='Reportes')
    #report_id = fields.Many2one('zue_curso.report_proveedores', string='Reporte asociado')

    _sql_constraints = [
        ('proveedor_unique','UNIQUE(type_document,num_document)','Ya existe un proveedor con este número y tipo de documento.'),
        ('proveedor_check_value','CHECK(value>=100)','El valor debe ser mayor o igual a 100.'),
    ]

    @api.constrains('type_proveedor','value')
    def _validate_proveedor(self):
        for record in self:
            if record.type_proveedor == 'a':
                if record.value < 200:
                    raise ValidationError('El tipo de proveedor adquiriente no puede tener un valor inferior a 200.')
            elif record.type_proveedor == 'b':
                if record.value < 300:
                    raise ValidationError('El tipo de proveedor prestamista no puede tener un valor inferior a 300.')
            elif record.type_proveedor == 'c':
                if record.value < 500:
                    raise ValidationError('El tipo de proveedor publico no puede tener un valor inferior a 500.')
            else:
                if record.value < 100:
                    raise ValidationError('El proveedor no puede tener un valor inferior a 100.')

    @api.constrains('report_ids')
    def _validate_reports_proveedor(self):
        for record in self:
            if len(record.report_ids) == 0:
                raise ValidationError('El proveedor debe tener asociado al menos un reporte.')

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id,f'{record.complate_name} - Valor:{str(record.value)}'))
        return result

class zue_curso_report_proveedores(models.Model):
    _name = 'zue_curso.report_proveedores'
    _description = 'Reporte de Proveedores del curso'

    name = fields.Char(string='Nombre reporte',required=True)
    solicitante = fields.Char(string='Solicitante', required=True)
    fecha_expedicion = fields.Datetime(string='Fecha de expedición')
    proveedor_ids = fields.Many2many('zue_curso.proveedores',string='Proveedores')
    #proveedor_ids = fields.One2many('zue_curso.proveedores','report_id',string='Proveedores asociados')

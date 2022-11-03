from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class res_country_state(models.Model):
    _inherit = 'res.country.state'

    code_dian = fields.Char(string='Code DIAN')

class res_partner(models.Model):
    _inherit = 'res.partner'

    is_proveedor = fields.Boolean(string='Es proveedor?')
    type_proveedor = fields.Selection([('a', 'Adquiriente'), ('b', 'Prestamista'), ('c', 'Publico')], string='Tipo proveedor')

    def create_proveedor(self):
        for record in self:
            if record.is_proveedor:
                type_document = 'NIT' if record.type_proveedor in ['b','c'] else 'CC'
                for contact in record.child_ids:
                    dict_proveedor = {
                        'complate_name':contact.name,
                        'type_document':type_document,
                        'num_document':contact.mobile,
                        'date_vinculation':fields.Date.today(),
                        'active': True,
                        'type_proveedor':record.type_proveedor,
                        'value': 2000,
                        'partner_id': record.id,
                    }
                    obj_proveedor = self.env['zue_curso.proveedores'].create(dict_proveedor)
                    print('--------------------------------')
                    print(f'Proveedor ({obj_proveedor.id}): ')
                    print(obj_proveedor.complate_name)
                    print(obj_proveedor.date_vinculation)
            else:
                raise ValidationError('El contacto no esta definido como proveedor')

    def create_report_proveedores(self):
        for record in self:
            if record.is_proveedor:
                obj_proveedores = self.env['zue_curso.proveedores'].search([('partner_id','=',record.id)])
                if len(obj_proveedores) == 0:
                    record.create_proveedor()
                    obj_proveedores = self.env['zue_curso.proveedores'].search([('partner_id', '=', record.id)])
                #Operaciones
                #obj_proveedores_state = obj_proveedores.filtered(lambda x: x.state == 'process')
                #obj_proveedores_map = obj_proveedores.mapped('complate_name')
                #obj_proveedores_map_lambda = obj_proveedores.mapped(lambda x: x.value + x.porc_a_reconocer)
                #obj_proveedores_sort = obj_proveedores.sorted(key=lambda x: x.complate_name)
                #Continuación metodo normal
                obj_report = self.env['zue_curso.report_proveedores'].search([('name', '=', 'Reporte contactos')])
                if len(obj_report) == 0:
                    dict_reporte = {
                        'name': 'Reporte contactos',
                        'solicitante': 'Curso ZUE',
                        'fecha_expedicion': fields.Date.today(),
                    }
                    obj_report = self.env['zue_curso.report_proveedores'].create(dict_reporte)
                dict_update = {
                    'proveedor_ids': obj_report.proveedor_ids.ids + obj_proveedores.ids
                }
                obj_report.write(dict_update)

    def delete_proveedor(self):
        for record in self:
            obj_proveedores = self.env['zue_curso.proveedores'].search([('partner_id', '=', record.id)])
            if len(obj_proveedores) == 0:
                raise ValidationError('No existen proveedores a eliminar.')
            else:
                obj_proveedores.unlink()


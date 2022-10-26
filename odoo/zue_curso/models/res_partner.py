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
                dict_proveedor = {
                    'complate_name':record.name,
                    'type_document':type_document,
                    'num_document':record.vat,
                    'date_vinculation':fields.Date.today(),
                    'active': True,
                    'type_proveedor':record.type_proveedor,
                    'value': 2000,
                }
                self.env['zue_curso.proveedores'].create(dict_proveedor)
            else:
                raise ValidationError('El contacto no esta definido como proveedor')


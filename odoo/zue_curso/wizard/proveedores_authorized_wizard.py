from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

class zue_curso_proveedores_authorized_wizard(models.TransientModel):
    _name = 'zue_curso.proveedores_authorized_wizard'
    _description = 'Wizard de autorización proveedores'

    proveedor_id = fields.Many2one('zue_curso.proveedores',string='Proveedor', required=True)
    user_id = fields.Many2one('res.users',string='Usuario que autoriza',required=True)
    description = fields.Text(string='Motivo')

    def execute_authorized(self):
        for record in self:
            if record.proveedor_id:
                message = '''
                    <p>----Autorización-----</p>
                    <p>Usuario: %s</p>
                    <p>Motivo: %s</p>
                ''' % (record.user_id.partner_id.name,record.description)
                record.proveedor_id.message_post(body=message)
                record.proveedor_id.write({'state':'process'})





from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class zue_curso_products(models.Model):
    _name = 'zue.curso.products'
    _description = 'Productos ZUE curso'
    _rec_name = 'description'

    code = fields.Char(string='Código', required=True)
    description = fields.Char(string='Descripción', required=True)
    type_product = fields.Selection([('con','Consumible'),
                                     ('alm','Almacenable'),
                                     ('ser','Servicio')], string='Tipo de producto', default='con')
    unit_price = fields.Float(string='Precio unitario')
    unif_measure = fields.Selection([('lb','Libras'),
                                     ('kg','Kilos'),
                                     ('cm','Centimetros'),
                                     ('uni','Unidad')],string='Unidad de medida', default='uni')
    brand = fields.Char(string='Marca')
    country_id = fields.Many2one('res.country',string='País de procedencia')
    attributes_ids = fields.One2many('zue.curso.products.attributes','product_id',string='Atributos')
    observations = fields.Text(string='Observaciones')

    _sql_constraints = [
        ('zue_curso_products_unique','UNIQUE(code)','Ya existe un producto con este código, por favor verifique.')
    ]

class zue_curso_products_attributes(models.Model):
    _name = 'zue.curso.products.attributes'
    _description = 'Atributos de Productos ZUE curso'

    product_id = fields.Many2one('zue.curso.products',string='Producto', required=True)
    name = fields.Char(string='Nombre', required=True)
    info = fields.Char(string='Información / Valor')
    additional_value = fields.Float(string='Valor adicional', help='Este valor sera sumado al precio unitario del producto')
    brand = fields.Char(string='Marca')


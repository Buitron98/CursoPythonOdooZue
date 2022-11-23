# -*- coding: utf-8 -*-
from odoo.http import request, route, Controller

class ZueCurso(Controller):

    @route('/zue_curso', auth='public', website=True)
    def index(self, **kw):
        if request.env.user:
            name = request.env.user.partner_id.name

        obj_proveedores = request.env['zue_curso.proveedores'].sudo().search([])

        return request.render('zue_curso.index_page',{'name_user':name,
                                                      'obj_proveedores':obj_proveedores})

    @route('/zue_curso/proveedor/show/<int:id>', auth='user', website=True)
    def show_proveedor(self, id):
        obj_proveedor = request.env['zue_curso.proveedores'].sudo().search([('id', '=', id)])

        return request.render('zue_curso.page_show_proveedor', {'proveedor': obj_proveedor})

    @route('/zue_curso/proveedor/edit/<int:id>', auth='user', website=True)
    def edit_proveedor(self, id):
        obj_proveedor = request.env['zue_curso.proveedores'].sudo().search([('id','=',id)])

        return request.render('zue_curso.page_edit_proveedor', {'proveedor': obj_proveedor})

    @route('/zue_curso/proveedor/edit_save', auth='user', website=True, csrf=False)
    def edit_proveedor_save(self, **kwargs):
        #Actualizar información
        dict_values = {
            'complate_name':kwargs['complate_name'],
            'value':float(kwargs['value']),
            'type_document':kwargs['type_document'],
            'num_document':kwargs['num_document'],
            'date_vinculation':kwargs['date_vinculation'],
        }
        obj_proveedor = request.env['zue_curso.proveedores'].sudo().search([('id', '=', kwargs['id'])])
        obj_proveedor.write(dict_values)
        #Enviar a pagina principal
        if request.env.user:
            name = request.env.user.partner_id.name

        obj_proveedores = request.env['zue_curso.proveedores'].sudo().search([])

        return request.render('zue_curso.index_page', {'name_user': name,
                                                       'obj_proveedores': obj_proveedores})

    @route('/zue_curso/proveedor/drop/<int:id>', auth='user', website=True)
    def drop_proveedor(self, id):
        obj_proveedor = request.env['zue_curso.proveedores'].sudo().search([('id', '=', id)])
        obj_proveedor.unlink()
        # Enviar a pagina principal
        if request.env.user:
            name = request.env.user.partner_id.name

        obj_proveedores = request.env['zue_curso.proveedores'].sudo().search([])

        return request.render('zue_curso.index_page', {'name_user': name,
                                                       'obj_proveedores': obj_proveedores})
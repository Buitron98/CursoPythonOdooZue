# -*- coding: utf-8 -*-
from odoo.http import request, route, Controller

class ZueCurso(Controller):

    @route('/zue_curso', auth='public', website=True)
    def index(self, **kw):
        if request.env.user:
            name = request.env.user.partner_id.name

        obj_proveedores = request.env['res.partner'].sudo().search([])

        return request.render('zue_curso.index_page',{'name_user':name,
                                                      'obj_proveedores':obj_proveedores})

#     @http.route('/zue_curso/zue_curso/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zue_curso.listing', {
#             'root': '/zue_curso/zue_curso',
#             'objects': http.request.env['zue_curso.zue_curso'].search([]),
#         })

#     @http.route('/zue_curso/zue_curso/objects/<model("zue_curso.zue_curso"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zue_curso.object', {
#             'object': obj
#         })

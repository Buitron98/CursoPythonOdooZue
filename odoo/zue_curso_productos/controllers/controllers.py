# -*- coding: utf-8 -*-
# from odoo import http


# class ZueCursoProductos(http.Controller):
#     @http.route('/zue_curso_productos/zue_curso_productos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zue_curso_productos/zue_curso_productos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zue_curso_productos.listing', {
#             'root': '/zue_curso_productos/zue_curso_productos',
#             'objects': http.request.env['zue_curso_productos.zue_curso_productos'].search([]),
#         })

#     @http.route('/zue_curso_productos/zue_curso_productos/objects/<model("zue_curso_productos.zue_curso_productos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zue_curso_productos.object', {
#             'object': obj
#         })

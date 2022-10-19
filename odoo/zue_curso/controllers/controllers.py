# -*- coding: utf-8 -*-
# from odoo import http


# class ZueCurso(http.Controller):
#     @http.route('/zue_curso/zue_curso', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

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

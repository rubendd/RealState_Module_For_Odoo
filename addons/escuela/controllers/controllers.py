# -*- coding: utf-8 -*-
# from odoo import http


# class Escuela(http.Controller):
#     @http.route('/escuela/escuela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuela/escuela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuela.listing', {
#             'root': '/escuela/escuela',
#             'objects': http.request.env['escuela.escuela'].search([]),
#         })

#     @http.route('/escuela/escuela/objects/<model("escuela.escuela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuela.object', {
#             'object': obj
#         })

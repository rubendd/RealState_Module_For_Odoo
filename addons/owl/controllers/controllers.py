# -*- coding: utf-8 -*-
# from odoo import http


# class Owl(http.Controller):
#     @http.route('/owl/owl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl/owl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl.listing', {
#             'root': '/owl/owl',
#             'objects': http.request.env['owl.owl'].search([]),
#         })

#     @http.route('/owl/owl/objects/<model("owl.owl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl.object', {
#             'object': obj
#         })

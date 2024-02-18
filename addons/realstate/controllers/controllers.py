# -*- coding: utf-8 -*-
# from odoo import http


# class Realstate(http.Controller):
#     @http.route('/realstate/realstate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/realstate/realstate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('realstate.listing', {
#             'root': '/realstate/realstate',
#             'objects': http.request.env['realstate.realstate'].search([]),
#         })

#     @http.route('/realstate/realstate/objects/<model("realstate.realstate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('realstate.object', {
#             'object': obj
#         })

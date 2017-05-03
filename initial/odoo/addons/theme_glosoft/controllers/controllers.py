# -*- coding: utf-8 -*-
from odoo import http

# class Glo-theme(http.Controller):
#     @http.route('/glo-theme/glo-theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/glo-theme/glo-theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('glo-theme.listing', {
#             'root': '/glo-theme/glo-theme',
#             'objects': http.request.env['glo-theme.glo-theme'].search([]),
#         })

#     @http.route('/glo-theme/glo-theme/objects/<model("glo-theme.glo-theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('glo-theme.object', {
#             'object': obj
#         })
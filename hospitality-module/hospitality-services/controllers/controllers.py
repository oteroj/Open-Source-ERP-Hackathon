# -*- coding: utf-8 -*-
from odoo import http

# class Hospitality-services(http.Controller):
#     @http.route('/hospitality-services/hospitality-services/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospitality-services/hospitality-services/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospitality-services.listing', {
#             'root': '/hospitality-services/hospitality-services',
#             'objects': http.request.env['hospitality-services.hospitality-services'].search([]),
#         })

#     @http.route('/hospitality-services/hospitality-services/objects/<model("hospitality-services.hospitality-services"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospitality-services.object', {
#             'object': obj
#         })
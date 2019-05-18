# -*- coding: utf-8 -*-
from odoo import http

# class HospitalityServices(http.Controller):
#     @http.route('/hospitality_services/hospitality_services/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospitality_services/hospitality_services/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospitality_services.listing', {
#             'root': '/hospitality_services/hospitality_services',
#             'objects': http.request.env['hospitality_services.hospitality_services'].search([]),
#         })

#     @http.route('/hospitality_services/hospitality_services/objects/<model("hospitality_services.hospitality_services"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospitality_services.object', {
#             'object': obj
#         })
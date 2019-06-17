# -*- coding: utf-8 -*-
from odoo import http

# class DhDashboard(http.Controller):
#     @http.route('/dh_dashboard/dh_dashboard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_dashboard/dh_dashboard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_dashboard.listing', {
#             'root': '/dh_dashboard/dh_dashboard',
#             'objects': http.request.env['dh_dashboard.dh_dashboard'].search([]),
#         })

#     @http.route('/dh_dashboard/dh_dashboard/objects/<model("dh_dashboard.dh_dashboard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_dashboard.object', {
#             'object': obj
#         })
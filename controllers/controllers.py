# -*- coding: utf-8 -*-
# from odoo import http


# class MayaReport(http.Controller):
#     @http.route('/maya_report/maya_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maya_report/maya_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('maya_report.listing', {
#             'root': '/maya_report/maya_report',
#             'objects': http.request.env['maya_report.maya_report'].search([]),
#         })

#     @http.route('/maya_report/maya_report/objects/<model("maya_report.maya_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maya_report.object', {
#             'object': obj
#         })

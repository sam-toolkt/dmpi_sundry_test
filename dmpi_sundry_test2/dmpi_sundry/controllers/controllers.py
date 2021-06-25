# -*- coding: utf-8 -*-
# from odoo import http


# class DmpiSundryTest2(http.Controller):
#     @http.route('/dmpi_sundry_test2/dmpi_sundry_test2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dmpi_sundry_test2/dmpi_sundry_test2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dmpi_sundry_test2.listing', {
#             'root': '/dmpi_sundry_test2/dmpi_sundry_test2',
#             'objects': http.request.env['dmpi_sundry_test2.dmpi_sundry_test2'].search([]),
#         })

#     @http.route('/dmpi_sundry_test2/dmpi_sundry_test2/objects/<model("dmpi_sundry_test2.dmpi_sundry_test2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dmpi_sundry_test2.object', {
#             'object': obj
#         })

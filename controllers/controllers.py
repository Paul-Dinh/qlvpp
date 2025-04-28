# -*- coding: utf-8 -*-
# from odoo import http


# class Qlvpp(http.Controller):
#     @http.route('/qlvpp/qlvpp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qlvpp/qlvpp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qlvpp.listing', {
#             'root': '/qlvpp/qlvpp',
#             'objects': http.request.env['qlvpp.qlvpp'].search([]),
#         })

#     @http.route('/qlvpp/qlvpp/objects/<model("qlvpp.qlvpp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qlvpp.object', {
#             'object': obj
#         })


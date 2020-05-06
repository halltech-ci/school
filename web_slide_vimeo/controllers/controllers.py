# -*- coding: utf-8 -*-
# from odoo import http


# class WebSlideVimeo(http.Controller):
#     @http.route('/web_slide_vimeo/web_slide_vimeo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_slide_vimeo/web_slide_vimeo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_slide_vimeo.listing', {
#             'root': '/web_slide_vimeo/web_slide_vimeo',
#             'objects': http.request.env['web_slide_vimeo.web_slide_vimeo'].search([]),
#         })

#     @http.route('/web_slide_vimeo/web_slide_vimeo/objects/<model("web_slide_vimeo.web_slide_vimeo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_slide_vimeo.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
import odoo
import os
from odoo import http
from odoo.http import request
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
templateLoader = FileSystemLoader(searchpath=BASE_DIR + "/html")
env = Environment(loader=templateLoader)


class Todo(http.Controller):
    @http.route('/desk/index/', auth='public', csrf=False)
    def desk_index(self, **kw):
        cr, uid, context, pool = request.cr, odoo.SUPERUSER_ID, request.context, request.env
        values = {}

        users = pool['res.users'].sudo().browse(request.session.uid)
        values['users'] = users

        template = env.get_template('/page1/index.html')
        html = template.render(object=values)
        return html

    @http.route('/desk/data/', auth='public', csrf=False)
    def desk_data(self, **kw):
        cr, uid, context, pool = request.cr, odoo.SUPERUSER_ID, request.context, request.env
        return "hello world"
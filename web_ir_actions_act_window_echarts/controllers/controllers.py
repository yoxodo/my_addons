# -*- coding: utf-8 -*-
from odoo import http

class WebIrActionsActWindowEcharts(http.Controller):
    @http.route('/web/sales_report_chart/')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/web_ir_actions_act_window_echarts/web_ir_actions_act_window_echarts/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('web_ir_actions_act_window_echarts.listing', {
            'root': '/web_ir_actions_act_window_echarts/web_ir_actions_act_window_echarts',
            'objects': http.request.env['web_ir_actions_act_window_echarts.web_ir_actions_act_window_echarts'].search([]),
        })

    @http.route('/web_ir_actions_act_window_echarts/web_ir_actions_act_window_echarts/objects/<model("web_ir_actions_act_window_echarts.web_ir_actions_act_window_echarts"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('web_ir_actions_act_window_echarts.object', {
            'object': obj
        })
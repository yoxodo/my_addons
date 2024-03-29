# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoCategory(models.Model):
    _name = 'todo.category'
    _description = '分类'

    name = fields.Char(u'名称')
    task_ids = fields.One2many('todo.task', 'category_id', string=u'待办事项')
    count = fields.Integer(u'任务数量', compute='_compute_task_count')

    @api.depends('task_ids')
    @api.multi
    def _compute_task_count(self):
        for record in self:
            record.count = len(record.task_ids)


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = '待办事项'

    name = fields.Char('描述', required=True)
    is_done = fields.Boolean('已完成？')
    priority = fields.Selection([
        ('todo', '待办'),
        ('normal', '普通'),
        ('urgency', '紧急')
    ], default='todo', string='紧急程度')
    deadline = fields.Datetime(u'截止时间')
    is_expired = fields.Boolean(u'已过期', compute='_compute_is_expired')
    category_id = fields.Many2one('todo.category', string=u'分类')
    detail_id = fields.One2many('todo.task_detail', 'header_id', string=u'明细')

    @api.depends('deadline')
    @api.multi
    def _compute_is_expired(self):
        for record in self:
            if record.deadline:
                record.is_expired = record.deadline < fields.Datetime.now()
            else:
                record.is_expired = False

    @api.multi
    def to_do_compare(self):
        self.ensure_one()
        context = self._context
        # Validation is skipped for brevity
        selection = context['o2m_selection']
        # do things with selection data
        compare_list = self.env['todo.task_detail_compare']
        detail_list = self.env['todo.task_detail']
        result = compare_list.search([])
        for record in result:
            record.unlink()

        for res_id in selection['detail_id']['ids']:
            domain = [('id', '=', res_id)]
            result = detail_list.search(domain, limit=1)
            record = {
                'detail_id': result.id,
                'name': result.name,
                'is_done': result.is_done,
                'deadline': result.deadline,
            }
            compare_list.write(record)
        result = {
            'name': 'test',
            'type': 'ir.actions.act_window',
            'res_model': 'todo.task_detail_compare',
            'view_mode': 'tree',
            'view_id': self.env.ref('todo.todo_task_detail_compare').id,
            # 'views': [('todo_task_detail_compare', 'tree')],
            'res_id': False,
            'context': False,
            'target': 'current',
        }
        return result


class TaskDetail(models.Model):
    _name = 'todo.task_detail'
    _description = '待办事项明细'

    name = fields.Char('明细描述', required=True)
    is_done = fields.Boolean('已完成？')
    deadline = fields.Datetime(u'截止时间')
    header_id = fields.Many2one('todo.task', string=u'待办事项')


class CompareTaskDetail(models.Model):
    _name = 'todo.task_detail_compare'
    _description = '待办事项对比'

    name = fields.Char('明细描述', required=True)
    is_done = fields.Boolean('已完成？')
    deadline = fields.Datetime(u'截止时间')
    detail_id = fields.Integer('明细ID')

    _sql_constraints = [
        ('detail_id_unique', 'unique (detail_id)', "The values must be unique"),
    ]

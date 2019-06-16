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
        raise ValidationError(context)


class TaskDetail(models.Model):
    _name = 'todo.task_detail'
    _description = '待办事项明细'

    name = fields.Char('明细描述', required=True)
    is_done = fields.Boolean('已完成？')
    deadline = fields.Datetime(u'截止时间')
    header_id = fields.Many2one('todo.task', string=u'待办事项')

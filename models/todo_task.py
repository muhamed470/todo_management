from odoo import models , fields


class ToDoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char()
    task_name = fields.Char()
    assign_to_id = fields.Many2one('res.partner')
    due_date = fields.Date(tracking=1)
    description = fields.Text()
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In_Progress'),
        ('completed', 'Completed'),
    ], default='new')



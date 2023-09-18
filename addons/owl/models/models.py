# -*- coding: utf-8 -*-

from odoo import models, fields, api


class todo(models.Model):
    _name = "owl.todo"
    _description = "owl.todo"

    name = fields.Char()
    completed = fields.Boolean()
    color = fields.Char()

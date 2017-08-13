# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import models, fields


class ShipmentScheduleReport(models.TransientModel):
    # class fields are defined here
    _name = 'shipment.schedule.report'

    current_date = fields.Date(
        default=fields.Date.context_today
    )
    threshold_date = fields.Date()
    categ_name = fields.Char()

    # # Data fields, used to browse report data
    categ_id = fields.Many2one(
        comodel_name='product.category',
    )
    line_ids = fields.One2many(
        comodel_name='shipment.schedule.report.line',
        inverse_name='report_id'
    )

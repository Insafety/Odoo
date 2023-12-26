# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class PropertyAccount(models.Model):
    _inherit = 'account.account'
    building_id = fields.Many2one('insafety.property.building', string="Building to Distribute Costs")

    current_balance = fields.Float(compute='_compute_current_balance')

    def _compute_current_balance(self):
        balances = {
            read['account_id'][0]: read['balance']
            for read in self.env['account.move.line'].read_group(
                domain=[('account_id', 'in', self.ids), ('parent_state', '=', 'posted')],
                fields=['balance', 'account_id'],
                groupby=['account_id'],
            )
        }
        for record in self:
            record.current_balance = balances.get(record.id, 0)

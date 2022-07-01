from odoo import models, fields
import datetime


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _compute_scheduled_date(self):
        for picking in self:
            picking.scheduled_date = datetime.date.today()
            picking.move_line_ids.date=datetime.date.today()

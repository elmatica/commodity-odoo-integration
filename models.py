from openerp import api, models, exceptions, fields,  _
import openerp.addons.decimal_precision as dp
from openerp.osv import osv
import logging
import datetime

_logger = logging.getLogger(__name__)

class product_template(models.Model):
	_inherit = 'product.template'

	@api.one
	def _compute_commodity_url(self):
		if self.commodity_id:
			parameter = self.env['ir.config_parameter'].search([('key','=','COMMODITY_URL')])
			if parameter:
				self.commodity_url = parameter.value + self.commodity_id

	commodity_id = fields.Char('Commodity ID',help='Commodity ID in commodity.live')
	commodity_url = fields.Char('Commodity URL',compute=_compute_commodity_url)

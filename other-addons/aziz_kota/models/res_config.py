from odoo import api, fields, models
from datetime import datetime

class ResConfig(models.TransientModel):
    _inherit = "res.config.settings"

    rajaongkir_api_key = fields.Char(string="RajaOngkir API Key")


    def set_values(self):
        res = super(ResConfig, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('rajaongkir_api_key', self.rajaongkir_api_key)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfig, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            rajaongkir_api_key=params.get_param('rajaongkir_key_api')
        )
        return res

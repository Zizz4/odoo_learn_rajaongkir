from odoo import api, fields, models

class Province(models.Model):
    _inherit = 'res.country.state'

    rajaongkir_province_id = fields.Integer(
        string="ID Provinsi RajaOngkir",
        index=True,
    )

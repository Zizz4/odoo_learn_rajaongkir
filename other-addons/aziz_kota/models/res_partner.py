from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one(
        comodel_name="aziz_kota.kota",
        string="Kota / Kabupaten",
        domain="[('state_id', '=', state_id)]"
    )

    kecamatan_id = fields.Many2one(
        comodel_name="aziz_kota.kecamatan",
        string="Kecamatan",
        domain="[('city_id', '=', city_id)]"
    )

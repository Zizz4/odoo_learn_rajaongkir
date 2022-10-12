from odoo import api, fields, models


class Kota(models.Model):
    _name = 'aziz_kota.kota'
    _description = 'Data Kota / Kabupaten'

    name = fields.Char(
        string='Nama Kota',
        required=True,
        index=True
    )

    description = fields.Text(
        string='Deskripsi',
    )

    active = fields.Boolean(
        string='Status',
        default=True,
    )

    state_id = fields.Many2one(
        comodel_name='res.country.state',
        string='Province',
        required=False,
    )

    kecamatan_ids = fields.One2many(
        comodel_name='aziz_kota.kecamatan',
        inverse_name='city_id',
        string='Data Kecamatan',

    )

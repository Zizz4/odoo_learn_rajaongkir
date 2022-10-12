from odoo import api, fields, models


class Kecamatan(models.Model):
    _name = 'aziz_kota.kecamatan'
    _description = 'Data Kecamatan'

    name = fields.Char(
        string='Nama Kecamatan',
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

    city_id = fields.Many2one(
        comodel_name="aziz_kota.kota",
        string="Kota / Kabupaten",
        required=False,
    )

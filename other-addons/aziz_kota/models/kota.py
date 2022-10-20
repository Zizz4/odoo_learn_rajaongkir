from odoo import api, fields, models
import requests


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

    rajaongkir_kota_id = fields.Integer(
        string="ID kota RajaOngkir",
        index=True
    )

    # url API RajaOngkir
    def get_end_point(self):
        return 'https://api.rajaongkir.com/starter/'

    # Key API
    def get_api_key(self):
        key = self.env['ir.config_parameter'].search([('key', '=', 'rajaongkir_api_key')])[0]['value']
        return key

    def action_generate_kota(self):
        header = {'key': self.get_api_key()}
        respon = requests.get(self.get_end_point() + 'city', headers=header)
        respon_json = respon.json()
        results = respon_json['rajaongkir']['results']

    def action_generate_province(self):
        header = {'key': self.get_api_key()}
        respon = requests.get(self.get_end_point() + 'province', headers=header)
        respon_json = respon.json()
        results = respon_json['rajaongkir']['results']

        for prov in results:
            existing = self.env['res.country.state'].search([('name', '=', prov['province'])])
            if existing:
                # update
                existing.rajaongkir_province_id = prov['province_id']
            else:
                # create
                vals = {
                    'name': prov['province'],
                    'code': prov['province'],
                    'rajaongkir_province_id': prov['province_id'],
                    'country_id': 100  # Indonesia
                }
                self.env['res.country.state'].sudo().create(vals)

        return True

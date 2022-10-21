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

    postal_code = fields.Char(
        string="Postal Code",

    )

    # url API RajaOngkir
    def get_end_point(self):
        return 'https://api.rajaongkir.com/starter/'

    # Key API
    def get_api_key(self):
        key = self.env['ir.config_parameter'].search([('key', '=', 'rajaongkir_api_key')])[0]['value']
        return key

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

    def action_generate_kota(self):
        header = {'key': self.get_api_key()}
        respon = requests.get(self.get_end_point() + 'city?id=&province=9', headers=header)
        respon_json = respon.json()
        results = respon_json['rajaongkir']['results']

        def get_state_id(rajaongkir_province_id):
            state = self.env['res.country.state'].search([('rajaongkir_province_id', '=', rajaongkir_province_id)])
            if state:
                return state.id
            else:
                return None

        for city in results:
            existing = self.env['aziz_kota.kota'].search([('name', '=', city['city_name'])])
            if existing:
                # update
                existing.rajaongkir_kota_id = city['city_id']
                existing.postal_code = city['postal_code']
            else:
                # create
                vals = {
                    'name': city['city_name'],
                    'postal_code': city['postal_code'],
                    'rajaongkir_kota_id': city['city_id'],
                    'state_id': get_state_id(city['province_id'])
                }
                self.env['aziz_kota.kota'].sudo().create(vals)
        return True

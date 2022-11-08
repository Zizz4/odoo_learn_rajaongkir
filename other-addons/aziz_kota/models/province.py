from odoo import api, fields, models
import requests

class Province(models.Model):
    _inherit = 'res.country.state'

    rajaongkir_province_id = fields.Integer(
        string="ID Provinsi RajaOngkir",
        index=True,
    )

    # url API RajaOngkir
    def get_end_point(self):
        return 'https://api.rajaongkir.com/starter/'

    # Key API
    def get_api_key(self):
        key = self.env['ir.config_parameter'].search([('key', '=', 'rajaongkir_api_key')])[0]['value']
        return key

    # @api.one
    def generate_kota_rajaongkir(self):

        self.ensure_one()

        header = {'key': self.get_api_key()}
        respon = requests.get(self.get_end_point() + 'city?id=&province={}'.format(self.rajaongkir_province_id), headers=header)
        respon_json = respon.json()
        results = respon_json['rajaongkir']['results']

        for city in results:
            existing = self.env['aziz_kota.kota'].search([('name', '=', city['city_name'])])
            if existing:
                # update
                existing.rajaongkir_kota_id = city['city_id']
            else:
                # create
                vals = {
                    'name': city['city_name'],
                    'postal_code': city['postal_code'],
                    'rajaongkir_kota_id': city['city_id'],
                    'state_id': self.id,

                }
                self.env['aziz_kota.kota'].sudo().create(vals)
        return True

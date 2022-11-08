from odoo import api, fields, models


class StateWizard(models.TransientModel):
    _name = 'aziz_kota.wizard'
    _description = 'Wizard generate kota rajaongkir'

    state_id = fields.Many2one(
        comodel_name='res.country.state',
        string="Province",
        required=True,
    )

    def generate_kota(self):
        return {}

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.tools import float_is_zero, html_keep_url, is_html_empty


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _default_note_url(self):
        return self.env.company.get_base_url()

    @api.model
    def _default_note(self):
        use_invoice_terms = self.env['ir.config_parameter'].sudo().get_param('account.use_invoice_terms')
        if use_invoice_terms and self.env.company.terms_type == "html":
            baseurl = html_keep_url(self._default_note_url() + '/terms')
            return _('Terms & Conditions: %s', baseurl)
        data = self.env.company.invoice_terms
        nama = self.env.user.name
        no_hp = self.env.user.work_phone

        if 'nama' in data:
            dataakhir = data.replace('nama', nama)
            if 'no_hp' in dataakhir:
                data_hp = no_hp
                dataakhir2 = dataakhir.replace("no_hp", str(data_hp))
                if 'False' in dataakhir2:
                    data_hp = "-"
                    dataakhir3 = dataakhir.replace("no_hp", data_hp)
                    return use_invoice_terms and dataakhir3 or ''
                else:
                    return use_invoice_terms and dataakhir2 or ''
            else:
                return use_invoice_terms and dataakhir or ''

    def action_refresh_terms(self):
        data = self.note
        nama = self.user_id.name
        no_hp = self.user_id.phone
        if 'nama' in data:
            data = data.replace("nama", str(nama))
            if 'no_hp' in data:
                data = data.replace("no_hp", str(no_hp))
                if 'False' in data:
                    data_hp = "-"
                    data = data.replace("False", data_hp)

        self.note = data

    note = fields.Html('Terms and conditions', default=_default_note)

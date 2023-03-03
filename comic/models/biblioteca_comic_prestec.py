from . import biblioteca_comic
from . import biblioteca_soci
from odoo import models, fields, api
class BibliotecaComicPrestec(models.Model):
    _name = 'biblioteca.comic.prestec'
    _inherit = 'biblioteca.comic'
    sociId = fields.Many2one('res.partner', string='Soci')
    dataInici = fields.Date('Data inici')
    dataFinal = fields.Date('Data final')
    @api.constrains('dataInici', 'dataFinal')
    def _check_release_date(self):
        for record in self:
            if record.dataInici and record.dataInici > fields.Date.today():
                raise models.ValidationError('La data de prestec no pot ser superior a la actual')
            if record.dataFinal and record.dataFinal < fields.Date.today():
                raise models.ValidationError('La data de tornada no pot ser inferior a la actual')

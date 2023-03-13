from odoo import models, fields, api

class diagnostic(models.Model):
	_name = 'diagnostic'
	diag = fields.Char('Diagnostic')
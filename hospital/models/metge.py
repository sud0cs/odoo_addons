from odoo import models, fields, api

class metge(models.Model):
	
	_name = 'metge'

	nom = fields.Char('Nom i cognoms')

	numero = fields.Integer('Numero colegiat') 
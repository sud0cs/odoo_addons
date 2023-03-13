from odoo import models, fields, api

class pacient(models.Model):
	
	_name = 'pacient'

	nom = fields.Char('Nom i cognoms')
	simptomes = fields.Char('Simptomes')

	
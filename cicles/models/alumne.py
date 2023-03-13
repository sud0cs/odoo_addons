from odoo import models, fields, api

class alumne(models.Model):
	
	_name = 'alumne'

	nom = fields.Char('Nom i cognoms')
from odoo import models, fields, api

class profesor(models.Model):
	_name = 'profesor'
	
	nom = fields.Char('Nom i cognoms')
from odoo import models, fields, api

class modul(models.Model):
	
	_name = 'modul'

	nom = fields.Char('Nom modul')
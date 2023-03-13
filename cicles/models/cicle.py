from odoo import models, fields, api

class cicle(models.Model):
	_name = 'cicle'
	
	nom = fields.Char('Nom cicle')
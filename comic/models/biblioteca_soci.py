# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api


# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo BibliotecaComic
# Y se ha creado puramente con fin didáctico para ver herencia entre modelos
class BibliotecaSoci(models.Model):
    _name = 'biblioteca.soci'
    _description = 'Socio de biblioteca'
    #id = fields.Integer('ID', required=True, index=True)
    nom = fields.Char('Nom', required=True)
    cognom = fields.Char('Cognom', required=True)


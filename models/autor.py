from odoo import models, fields, api

class Autor(models.Model):
    _name = 'library.autor'
    _description = 'Modelo autor del libro'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Author", required=True)

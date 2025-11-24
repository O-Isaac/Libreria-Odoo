from odoo import models, fields, api

class Libro(models.Model):
    _name = 'library.libro'
    _description = 'Modelo del libro en el estante'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()

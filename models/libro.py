from odoo import models, fields, api

class Libro(models.Model):
    _name = 'library.libro'
    _description = 'Modelo del libro en el estante'

    title = fields.Char(string="Título del libro", required=True, help="Título del libro")
    description = fields.Text(string="Sipnosis corta del libro")
    pages = fields.Integer(string="Paginas del libro", required=True, default=0)
    price = fields.Float(string="Precio del libro", digits=(10, 2), required=True)
    is_avalible = fields.Boolean(string="¿Disponible?", default=False)
    public_date = fields.Date(string="Fecha de publicacion")
    created_timestamp = fields.Datetime(string="Fecha de creacion", default=fields.Datetime.now)
    image = fields.Image(string="Imagen del libro", max_width=150, max_height=150)
    author = fields.Char(string="Autor", required=True, default="Desconocido")
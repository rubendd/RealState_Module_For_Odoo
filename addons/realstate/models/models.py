# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'realstate.property'
    _description = 'Property'

    name = fields.Char(string = 'Nombre', required=True)
    description = fields.Text(string = 'Descripcion')
    postcode = fields.Char(string = 'Postcode')
    date_availability = fields.Date(string = 'Fecha disponible')
    expected_price = fields.Float(required=True, string = 'Precio esperado')
    selling_price = fields.Float(string = 'Precio')
    bedrooms = fields.Integer(string = 'Camas')
    living_area = fields.Integer(string = 'Sala de estar')
    facades = fields.Integer(string = 'Fachadas')
    garage = fields.Boolean(string = 'Garage')
    garden = fields.Boolean(string = 'Jardín')
    garden_area = fields.Integer(string = 'Area jardín')
    total = fields.Float(compute="_compute_total_area")
    amount = fields.Float()


    garden_orientation = fields.Selection(
        string = 'Orientación del jardín',
        selection = [
            ('north','North'),
            ('south','South'),
            ('east','East'),
            ('west','West')
            ],
        )        

    ## relaciones
    property_type_id = fields.Many2one('realstate.type', string='Tipo de propiedad')
    buyer = fields.Many2one('res.partner', string='Comprador')
    user = fields.Many2one('res.users', string='Agente inmobiliario')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total = record.living_area + record.garden_area

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price and record.selling_price < record.expected_price:
                raise ValidationError("El precio de venta no puede ser menor que el precio esperado.")        


class Type(models.Model):
    _name = 'realstate.type'
    _description = 'Types'

    name = fields.Char(string = 'Nombre', required=True)    

    

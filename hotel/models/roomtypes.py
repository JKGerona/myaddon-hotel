from odoo import models, fields

class HotelRoomTypes(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'Hotel Room Types'

    name = fields.Char(string="Room Type", required=True)
    description = fields.Char(string="Room Type Description")
    room_image = fields.Binary(string="Room Image")
    bathroom_image = fields.Binary(string="Bathroom Image")
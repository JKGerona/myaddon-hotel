from odoo import models, fields

class HotelRooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'Hotel Rooms'

    name = fields.Char(string="Room Name", required=True)
    description = fields.Text(string="Description")
    room_type_id = fields.Many2one('hotel.roomtypes', string="Room Type")

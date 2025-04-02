from odoo import models, fields

class HotelRooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'Hotel Rooms'

    name = fields.Char(string='Room Name', required=True)
    room_number = fields.Char(string='Room Number', required=True)
    # ...existing fields...

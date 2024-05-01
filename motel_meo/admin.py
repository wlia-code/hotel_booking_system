from django.contrib import admin
from .models import Hotel, Room, Booking

# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Hotel model.
    """
    list_display = ("name", "location", "state")
    search_fields = ("name",)
    list_filter = ("name", "location")

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Room model.
    """
    list_display = ("room_no", "room_type", "status", "price", "hotel")
    search_fields = ("room_no",)
    list_filter = ("room_no", "status")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Booking model.
    """
    list_display = ("room", "check_in", "check_out", "booking_id", "customer")
    search_fields = ("room", "customer", "booking_id")
    list_filter = ("room", "customer")

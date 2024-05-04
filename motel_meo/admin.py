from django.contrib import admin
from .models import Room, Amenity, Booking, Profile

admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(Booking)
admin.site.register(Profile)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Display the amenity name in the list view

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_type", "price", "capacity", "get_image_preview")
    search_fields = ("room_type",)
    list_filter = ("room_type", "price")  # Add filters
    readonly_fields = ("get_image_preview",) # Make image preview read-only

    def get_image_preview(self, obj):
        if obj.image:
            return '<img src="%s" style="max-width: 200px; max-height: 200px;" />' % obj.image.url
        else:
            return "No image available"

    get_image_preview.short_description = "Image Preview"
    get_image_preview.allow_tags = True # To allow HTML rendering

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("room", "customer", "check_in", "check_out", "get_nights")
    list_filter = ("room", "customer") 

    def get_nights(self, obj):
        if obj.check_in and obj.check_out:
            nights = (obj.check_out - obj.check_in).days
            return f"{nights} night(s)"
        else:
            return "-"
    get_nights.short_description = "Duration"

from django.db import models
from django.contrib.auth.models import User


class Amenity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_TYPES = (
        ('1', 'Single'),
        ('2', 'Double'),
        ('3', 'Suite'),
    )

    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='room_images', blank=True, null=True) 
    description = models.TextField(blank=True)
    amenities = models.ManyToManyField(Amenity)
    is_featured = models.BooleanField(default=False)


    def __str__(self):
        return f"Room Type: {self.room_type} - Price: {self.price}"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking for {self.customer} - Room: {self.room}"

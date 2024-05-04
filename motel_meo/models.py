
def get_bookings_by_user(request, user_id):
    bookings = Booking.objects.filter(customer_id=user_id)
    return bookings



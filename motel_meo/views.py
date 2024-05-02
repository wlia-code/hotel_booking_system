from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Room

def home(request):
    featured_rooms = Room.objects.filter(is_featured=True)[:3]
    context = {'featured_rooms': featured_rooms}
    return render(request, 'home.html', context)

def search_results(request):
    if request.method == "GET":
        # Retrieve search parameters from the form data
        location = request.GET.get('location')
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        room_type = request.GET.get('room_type')

        # Filter rooms based on search criteria
        filtered_rooms = Room.objects.filter(
            location=location,
            room_type=room_type
        ).exclude(
            Q(booking__check_in__lte=check_out, booking__check_out__gte=check_in) | 
            Q(booking__check_in__lte=check_out, booking__check_out__gte=check_out) |
            Q(booking__check_in__lte=check_in, booking__check_out__gte=check_in) |
            Q(booking__check_in__gte=check_in, booking__check_out__lte=check_out)
        )

        # Prepare a context dictionary with the results
        context = {
            'filtered_rooms': filtered_rooms,
            'location': location,
            'check_in': check_in,
            'check_out': check_out,
            'room_type': room_type
        }
        return render(request, 'search_results.html', context)
    else:
        # Handle cases where the request method is not GET
        return render(request, 'search_results.html')

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    context = {'room': room}
    return render(request, 'room_detail.html', context)
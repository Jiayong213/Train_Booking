from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from .models import Coach, Seat, Booking


def seating_plan(request):
    coaches = Coach.objects.all()
    return render(request, 'booking/seating_plan.html', {'coaches': coaches})


def book_seat(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)

    with transaction.atomic():
        if seat.is_locked:
            return render(request, 'booking/booking_failed.html', {'sear':seat})
        
        seat.is_locked = True
        seat.save()

        booking = Booking(seat=seat, user_name=request.user.username)
        booking.save()

    return render(request, 'booking/booking_success.html', {'seat':seat})
from django.db import models

class Coach(models.Model):
    coach_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Coach {self.coach_number}"

class Seat(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.coach.coach_number} - Seat {self.seat_number}"

class Booking(models.Model):
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} booked {self.seat}"
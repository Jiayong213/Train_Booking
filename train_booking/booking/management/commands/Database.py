from django.core.management.base import BaseCommand
from booking.models import Coach, Seat

class Command(BaseCommand):
    help = 'Populates the database with coaches and seats'

    def handle(self, *args, **kwargs):
        for i in range(1, 7):
            coach = Coach.objects.create(coach_number=f"C{i}")
            for j in range(1, 21):
                Seat.objects.create(coach=coach, seat_number=f"S{j}")
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
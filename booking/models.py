from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    available_seats = models.PositiveIntegerField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)


    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user.username} - {self.show.title} ({self.seats_booked} seats)"

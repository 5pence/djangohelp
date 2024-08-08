from django.db import models


class Booking(models.Model):
    TIMESLOT_CHOICES = [
        ("18:00", "6 PM"),
        ("19:00", "7 PM"),
        ("20:00", "8 PM"),
    ]

    TABLE_CHOICES = [
        ("1", "Window"),
        ("2", "Quiet"),
        ("3", "Music"),
    ]

    booking_date = models.DateTimeField()
    booking_time = models.CharField(max_length=5, choices=TIMESLOT_CHOICES)
    table_booked = models.CharField(max_length=10, choices=TABLE_CHOICES)

    class Meta:
        unique_together = [["booking_date", "booking_time", "table_booked"]]
        ordering = ["booking_date", "booking_time"]
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"Table {self.table_booked} booked on {self.booking_date} at {self.booking_time}"
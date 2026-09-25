from django.db import models
from rooms.models import Room

class Bed(models.Model):
    BED_STATUS = (
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='beds'
    )

    bed_number = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        choices=BED_STATUS,
        default='available'
    )

    def __str__(self):
        return f"{self.room.room_number} - {self.bed_number}"
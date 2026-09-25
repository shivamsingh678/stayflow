from django.db import models

from properties.models import Property



class Room(models.Model):


    property = models.ForeignKey(
    Property,
    on_delete=models.CASCADE,
    related_name='rooms'
)
    
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20)
    capacity = models.IntegerField()
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number
from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = (
        ('PG', 'PG'),
        ('HOSTEL', 'Hostel'),
        ('APARTMENT', 'Apartment'),
    )

    name = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    address = models.TextField()
    city = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=100)
    owner_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
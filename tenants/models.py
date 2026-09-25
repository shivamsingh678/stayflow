from django.db import models


class Tenant(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    address = models.TextField()

    emergency_contact = models.CharField(max_length=15)

    joining_date = models.DateField()

    def __str__(self):
        return self.full_name
from django.db import models
from tenants.models import Tenant


class Visitor(models.Model):

    visitor_name = models.CharField(
        max_length=100
    )

    phone_number = models.CharField(
        max_length=15
    )

    purpose = models.CharField(
        max_length=200
    )

    # Visitor create hote hi current date-time automatically save hoga
    entry_time = models.DateTimeField(
        auto_now_add=True
    )

    # Visitor jab exit kare tab update karenge
    exit_time = models.DateTimeField(
        null=True,
        blank=True
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.visitor_name
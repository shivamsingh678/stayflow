from django.db import models
from tenants.models import Tenant
from beds.models import Bed

class Allocation(models.Model):
    tenant = models.OneToOneField(
        Tenant,
        on_delete=models.CASCADE
    )

    bed = models.OneToOneField(
        Bed,
        on_delete=models.CASCADE
    )

    allocated_date = models.DateField()

    security_deposit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tenant.full_name} -> {self.bed}"
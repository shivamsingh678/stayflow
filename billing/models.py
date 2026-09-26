from django.db import models
from allocations.models import Allocation


class RentInvoice(models.Model):

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('partial', 'Partially Paid'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    )

    allocation = models.ForeignKey(
        Allocation,
        on_delete=models.CASCADE,
        related_name='rent_invoices'
    )

    billing_month = models.DateField()

    rent_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    electricity_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    maintenance_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    late_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    due_date = models.DateField()

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )

    def __str__(self):
        return f"{self.allocation.tenant.full_name} - {self.billing_month}"
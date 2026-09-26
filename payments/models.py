from django.db import models
from billing.models import RentInvoice


class Payment(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Cash'),
        ('upi', 'UPI'),
        ('bank', 'Bank Transfer'),
    )

    invoice = models.ForeignKey(
        RentInvoice,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField()

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    transaction_reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.invoice.id} - {self.amount}"
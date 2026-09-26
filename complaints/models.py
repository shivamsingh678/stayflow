from django.db import models
from tenants.models import Tenant

class Complaint(models.Model):

    CATEGORY_CHOICES = [
        ('Electricity', 'Electricity'),
        ('Plumbing', 'Plumbing'),
        ('Cleaning', 'Cleaning'),
        ('WiFi', 'WiFi'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Assigned', 'Assigned'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class ComplaintComment(models.Model):
    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.comment[:30]    
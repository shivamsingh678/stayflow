from rest_framework import viewsets
from .models import RentInvoice
from .serializers import RentInvoiceSerializer


class RentInvoiceViewSet(viewsets.ModelViewSet):
    queryset = RentInvoice.objects.all()
    serializer_class = RentInvoiceSerializer
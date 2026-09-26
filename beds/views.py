from rest_framework import viewsets
from .models import Bed
from .serializers import BedSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
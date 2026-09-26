from rest_framework import viewsets
from .models import Complaint, ComplaintComment
from .serializers import ComplaintSerializer, ComplaintCommentSerializer


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


class ComplaintCommentViewSet(viewsets.ModelViewSet):
    queryset = ComplaintComment.objects.all()
    serializer_class = ComplaintCommentSerializer
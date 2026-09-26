from rest_framework import serializers
#from .models import Complaint
from .models import Complaint, ComplaintComment

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


class ComplaintCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintComment
        fields = '__all__'        
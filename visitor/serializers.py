from rest_framework import serializers
from .models import *

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visitor_data
        fields='__all__'
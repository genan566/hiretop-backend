from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from .models import Employments

class EmploymentsSerializer(serializers.ModelSerializer):
    """Serializer for Employments"""
    
    class Meta:
        model = Employments
        fields = "__all__"
        read_only_fields = ("id",)


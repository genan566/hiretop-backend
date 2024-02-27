from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from .models import Enterprise

class EnterpriseSerializer(serializers.ModelSerializer):
    """Serializer for Enterprise"""
    
    class Meta:
        model = Enterprise
        fields = "__all__"
        read_only_fields = ("id",)


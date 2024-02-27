from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    """Serializer for Client"""
    
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ("id",)


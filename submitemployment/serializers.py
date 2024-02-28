from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from .models import SubmitEmployment

class SubmitEmploymentSerializer(serializers.ModelSerializer):
    """Serializer for SubmitEmployment"""
    
    class Meta:
        model = SubmitEmployment
        fields = "__all__"
        read_only_fields = ("id",)




class SubmitEmploymentFileSerializer(serializers.ModelSerializer):
    """Serializer for file uploading"""

    class Meta:
        model = SubmitEmployment
        fields = ("id", "cv_file")
        read_only_fields = ("id",)
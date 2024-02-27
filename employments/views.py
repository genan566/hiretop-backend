from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from custom_permissions.IsStaffUser import SomeModelPermission, IsAdminUser
from .models import Employments
from . import serializers

class EmploymentsViewSet(viewsets.ModelViewSet):
    """Manage Employments in the db"""
    authentication_classes = (TokenAuthentication,)
    queryset = Employments.objects.all().order_by('-id')
    serializer_class = serializers.EmploymentsSerializer
    pagination_class = None
    
    def get_queryset(self):
        """Retrieve the Employments from the query params sended"""

        return Employments.objects.all().order_by('-id')

    def perform_create(self, serializer):
        """Create a new object"""
        instance = serializer.save()


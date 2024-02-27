from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from custom_permissions.IsStaffUser import SomeModelPermission, IsAdminUser
from .models import SubmitEmployment
from . import serializers

class SubmitEmploymentViewSet(viewsets.ModelViewSet):
    """Manage SubmitEmployment in the db"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = SubmitEmployment.objects.all().order_by('-id')
    serializer_class = serializers.SubmitEmploymentSerializer
    pagination_class = None
    
    def get_queryset(self):
        """Retrieve the SubmitEmployment from the query params sended"""

        return SubmitEmployment.objects.all().order_by('-id')

    def perform_create(self, serializer):
        """Create a new object"""
        instance = serializer.save()


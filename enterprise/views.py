from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from custom_permissions.CanJustReadPermissions import CanJustReadOrPostPermission
from .models import Enterprise
from . import serializers

class EnterpriseViewSet(viewsets.ModelViewSet):
    """Manage Enterprise in the db"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CanJustReadOrPostPermission,)
    queryset = Enterprise.objects.all().order_by('-id')
    serializer_class = serializers.EnterpriseSerializer
    pagination_class = None
    
    def get_queryset(self):
        """Retrieve the Enterprise from the query params sended"""

        return Enterprise.objects.all().order_by('-id')

    def perform_create(self, serializer):
        """Create a new object"""
        instance = serializer.save()

    def get_queryset(self):
        """Retrieve the enterprise from the query params sended"""

        query_user = self.request.query_params.get("user")
        queryset = self.queryset

        if query_user:
            return queryset.filter(creator=query_user)

        return queryset
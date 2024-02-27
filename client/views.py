from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from custom_permissions.CanJustReadPermissions import CanJustReadOrPostPermission
from .models import Client
from . import serializers

class ClientViewSet(viewsets.ModelViewSet):
    """Manage Client in the db"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CanJustReadOrPostPermission,)
    queryset = Client.objects.all().order_by('-id')
    serializer_class = serializers.ClientSerializer
    pagination_class = None
    
    def get_queryset(self):
        """Retrieve the Client from the query params sended"""

        return Client.objects.all().order_by('-id')

    def perform_create(self, serializer):
        """Create a new object"""
        instance = serializer.save()

    def get_queryset(self):
        """Retrieve the client from the query params sended"""

        query_user = self.request.query_params.get("user")
        queryset = self.queryset

        if query_user:
            return queryset.filter(member=query_user)

        return queryset


from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from custom_permissions.CanJustReadPermissions import CanJustReadOrPostPermission
from .models import SubmitEmployment
from . import serializers

class SubmitEmploymentViewSet(viewsets.ModelViewSet):
    """Manage SubmitEmployment in the db"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CanJustReadOrPostPermission,)
    queryset = SubmitEmployment.objects.all().order_by('-id')
    serializer_class = serializers.SubmitEmploymentSerializer
    pagination_class = None
    lookup_field = "id"
    
    def get_queryset(self):
        """Retrieve the SubmitEmployment from the query params sended"""

        return SubmitEmployment.objects.all().order_by('-id')

    def perform_create(self, serializer):
        """Create a new object"""
        instance = serializer.save()


    def get_serializer_class(self):
        if self.action == "upload_cv":
            return serializers.SubmitEmploymentFileSerializer
        
        return self.serializer_class


    @action(methods=["POST"], detail=True, url_path="upload-cv")
    def upload_cv(self, request, id=None):
        """Upload image"""
        recipe = self.get_object()
        serializer = self.get_serializer(
            recipe,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
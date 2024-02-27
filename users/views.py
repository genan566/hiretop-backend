from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets, mixins
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.views import APIView
from . import serializers
from custom_permissions.CanJustReadPermissions import CanJustReadOrIsAdminPermission,IsAdmin2
from custom_permissions.CanJustReadPermissions import CanJustPostOrIsAdminPermission
from core.models import User
from custom_permissions.IsStaffUser import IsAdminUser,SomeModelPermission


class CreateUserView(generics.CreateAPIView):
    """ViewSet for creating user"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create authtoken for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            # 'user_id': user.pk,
            # 'email': user.email
        })

class ManageUserView(generics.RetrieveUpdateAPIView,
                     ):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_object(self):
        """"""
        return self.request.user

class ManageUserRetriveUpdateView(generics.RetrieveUpdateAPIView,
                                  ):
    """Manage the update/retrieve on user"""
    serializer_class = serializers.UserImageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_object(self):
        """"""
        return self.request.user

class ManageUserRetriveUpdateAuthView(generics.RetrieveUpdateAPIView,
                                  ):
    """Manage the update/retrieve on authenticated user"""
    serializer_class = serializers.UserImageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (CanJustReadOrIsAdminPermission,)
    queryset = User.objects.all()
    lookup_field = "id"

class ManageUserListView(generics.ListAPIView):
    """Manage the list user view"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (CanJustPostOrIsAdminPermission,)
    queryset = User.objects.all()
    lookup_field = "id"
    
    
    def get_queryset(self):
        """Retrieve the nfts from the query params sended"""

        query_by_active_client = self.request.query_params.get("active")
        queryset = User.objects.all()
        
        try:
            if int(query_by_active_client) == 1:
                queryset = User.objects.filter(is_staff=False,is_superuser=False)
                return queryset

        except:
            pass
        
        finally:
            return  queryset
            
        


class RetrieveUserView(APIView):
    """Manage the retrieve user view"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (SomeModelPermission,)

    def get_object(self, id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def get(self, request, id, *args, **kwargs):
        '''
        Getting user data
        '''
        todo_instance = self.get_object(id)
        if not todo_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = serializers.UserRetrieveSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, id, *args, **kwargs):
        '''
        Updates/replace user full data
        '''
        todo_instance = self.get_object(id)
        if not todo_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(instance=todo_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, *args, **kwargs):
        '''
        Patching user data
        '''
        todo_instance = self.get_object(id)
        if not todo_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(instance=todo_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, id, *args, **kwargs):
        '''
        Deletes the user data
        '''
        todo_instance = self.get_object(id)
        if not todo_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

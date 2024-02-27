from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serialize the users objects"""

    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "name", "is_staff",
                  # "is_active",
                  "is_superuser", "image",)
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ("id",)

    def create(self, validated_data):
        """Create requester"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Updating data for user"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Manage Token generation"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password
        )

        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return attrs


class UserImageSerializer(serializers.ModelSerializer):
    """Serializer for image uploading"""

    class Meta:
        model = User
        fields = ("id", "image", "email")
        read_only_fields = ("id", "email")


class UserRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for the retrieve user data"""

    class Meta:
        model = User
        fields = ("email", "name", "is_staff", "is_superuser",
                  "image", "id",)
        read_only_fields = ("id", "email")

from rest_framework import permissions
from rest_framework.permissions import IsAdminUser as BaseIsAdminUser

class SomeModelPermission(permissions.DjangoModelPermissions):
    message = "You can't use this endpoint if you are not staff user"
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_staff

        # other logic

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

        # other logic

class IsAdminUser(BaseIsAdminUser):
    message = "You can't use this endpoint if you are not staff/admin user"
    def has_object_permission(self, request, view, obj):
        # Just reuse the same logic as `has_permission`...
        return self.has_permission(request, view)
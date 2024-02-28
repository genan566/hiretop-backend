from rest_framework import permissions

class CanJustPostOrIsAdminPermission(permissions.DjangoModelPermissions):
    message = "You can't use this endpoint if you are not admin user"

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user.is_superuser

class CanJustReadOrIsAdminPermission(permissions.DjangoModelPermissions):
    message = "You can't use this endpoint if you are not admin user"

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_superuser


class UserIsNotSetPermission(permissions.DjangoModelPermissions):
    message = "You can't use this endpoint if you are not logged in"

    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user


class CanJustReadOrPostPermission(permissions.DjangoModelPermissions):
    message = "You can't use this endpoint if you are not admin user"

    def has_permission(self, request, view):
        if request.method == "GET" or request.method == "POST":
            return True
        return request.user.is_superuser



class CanJustPostPermission(permissions.DjangoModelPermissions):
    message = "You can't use this endpoint if you are not admin user"

    def has_permission(self, request, view):

        if request.method == "GET" or request.method == "POST" or request.method == "DELETE" or request.method == "PUT" or request.method == "PATCH":
            return request.user.is_staff or request.user.is_superuser

        return request.user != "AnonymousUser"


class IsAdmin2(permissions.DjangoModelPermissions):
    message = "You can't use this endpoint if you are not admin user"

    def has_permission(self, request, view):
        return request.user

# class CanJustReadOrPostPermission(permissions.DjangoModelPermissions):
#     message = "You can't use this endpoint if you are not admin user"
#
#     def has_permission(self, request, view):
#
#         if request.method == "GET" or request.method == "DELETE" or request.method == "PUT" or request.method == "PATCH":
#             return request.user.is_superuser
#
#         if request.method == "POST":
#             return True
#
#         return request.user != "AnonymousUser"

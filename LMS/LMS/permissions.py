from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

class UserOnlyEditAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.methods is permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user == obj.user)
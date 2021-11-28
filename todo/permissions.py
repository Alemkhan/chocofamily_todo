from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False

        return bool(request.user and request.user.role == 2)


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(request.user, AnonymousUser):
            return False

        return bool(request.user == obj.created_by or request.user.role == 1)

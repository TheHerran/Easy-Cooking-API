from rest_framework import permissions
from rest_framework.views import Request, View

from accounts.models import Account
from recipes.models import Recipe


class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Account):
        return obj == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Recipe):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

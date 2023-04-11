from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Account


class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Account):
        print(obj)
        print(request.user)
        return obj == request.user
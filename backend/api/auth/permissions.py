from rest_framework.permissions import BasePermission

ALLOWED_METHODS = ('HEAD', 'OPTIONS')


class AuthUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ALLOWED_METHODS:
            return True

        if request.method == 'POST':
            return not request.user.is_authenticated

        return request.user.is_authenticated

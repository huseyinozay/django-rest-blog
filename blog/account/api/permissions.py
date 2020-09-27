from rest_framework.permissions import BasePermission

class NotAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_authenticated

    message = 'You already have an account.'
    
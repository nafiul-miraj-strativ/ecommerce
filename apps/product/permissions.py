from rest_framework.permissions import BasePermission
from apps.user.models import User

class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user
            and user.is_authenticated
            and (user.is_superuser or user.role in [User.MANAGER, User.ADMIN])
        )
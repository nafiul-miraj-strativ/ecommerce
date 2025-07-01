from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return (
            request.user
            and request.user.is_authenticated
            and (request.user.is_superuser or request.user.role == 'admin')
        )   
class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'manager'
    
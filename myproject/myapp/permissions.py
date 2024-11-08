from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsExampleDomainUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.email.endswith('@example.com')
    
class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and getattr(user, 'role', None) == "admin":
            return True
        return False

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
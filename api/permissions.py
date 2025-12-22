from rest_framework import permissions


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Allows any authenticated user to GET, 
    but only superusers can POST.
    """
    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Check for superuser status for POST
        return bool(request.user and request.user.is_superuser)


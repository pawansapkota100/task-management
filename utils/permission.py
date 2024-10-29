from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsTaskOwner(permissions.BasePermission):
    """
    Custom permission to allow users to view their own tasks,
    and only allow the owner to update or delete their tasks.
    """

    def has_permission(self, request, view):
        # Allow read access to all users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # For write operations, the user must be authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # For read access, allow if the task was created by the user
        if request.method in permissions.SAFE_METHODS:
            if obj.created_by != request.user:
                raise PermissionDenied("You do not have permission to perform this operation.")
            return True
        
        # Allow update or delete only if the user is the creator of the task
        if obj.created_by != request.user:
            raise PermissionDenied("You do not have permission to perform this operation.")
        
        return True  # User is the creator, allow the action

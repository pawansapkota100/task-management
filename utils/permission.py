from rest_framework.permissions import BasePermission
from core.models import Task

class Isowner(BasePermission):
    def has_permission(self, request, view):
        if Task.created_by == request.user:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user

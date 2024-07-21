from rest_framework import permissions

class updateownprofile(permissions.BasePermission):
    """allow user to edit thier own profile"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id
        
class updateownstatus(permissions.BasePermission):
    """allow users update thierown status"""
    def has_object_permission(self, request, view, obj):
        """check the user is trying to update thierown status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.userprofile.id==request.user.id

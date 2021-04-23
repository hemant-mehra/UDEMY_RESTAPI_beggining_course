from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow uset to edit thier own profile"""
    
    def has_object_permission(self,request,view,obj):
        """check user is trying their own profile"""
        
        
        # safe methods are mehtod which doest change anything like get() so other user can use this method
        # we have to restrict only unsafe method like put post delete 
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # comparing ids of logged in user and obj which is being updated
        return obj.id == request.user.id
    


# crwated for feed 
class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update thier own status"""
    
    def has_object_permission(self,request,view,obj):
        """check user is trying their own status"""
        
        
        # safe methods are mehtod which doest change anything like get() so other user can use this method
        # we have to restrict only unsafe method like put post delete 
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # comparing ids of logged in user and obj which is being updated
        return obj.user_profile.id == request.user.id
from rest_framework.permissions import BasePermission, IsAuthenticated


class isForNormalUser(BasePermission):
    '''
    custom permission only allow user assgined promo to 
    deduct promo amout
    '''
    def has_object_permission(self, request, view, obj):
        user = request.user;
        method=request.method;
        if method=='PATCH':
            if user.is_authenticated and obj.user == user :
                return True;
        return False;
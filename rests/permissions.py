__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework.permissions import BasePermission
class IsOwnerOrReadOnly(BasePermission):
    message="You must be the owner "
    def has_object_permission(self, request, view, obj):
        print(request.user,'fff6fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
        print(obj.student_user,'fff6fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
        return obj.student_user==request.user
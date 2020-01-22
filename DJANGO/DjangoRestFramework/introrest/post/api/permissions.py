from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You must be the owner of this object."

    def has_permission(self, request,
                       view):  # has_object_permission'a girmeden önce burası çalışır ve her istek tipinde (post,get,delete..) çalışır
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
                       obj.user == request.user) or request.user.is_superuser  # nesnenin sahibi ise True veya admin ise True dönecek

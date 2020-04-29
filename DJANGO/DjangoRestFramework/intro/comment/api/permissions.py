from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):  # custom permission yazıyoruz
    message = "Bu işlemi sen yapamazsın"  # bu değişken (message) izne sahip değilse döner

    def has_permission(self, request, view):  # önce burayı kontrol eder ardından has_obj'e gider (opsiyonel) (giriş yapıldı mı vb. kontrolleri yapabiliriz)
        # print("çalıştı has_permission")
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):  # parametre olarak gelen obje istediğimiz izne sahip mi
        # print("çalıştı has_object_permission")
        return obj.user == request.user

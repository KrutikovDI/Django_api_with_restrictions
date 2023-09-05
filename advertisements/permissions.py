from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAutor(BasePermission):
    def has_object_permissions(self, request, view, obj):       # разграничиваем действия: для просмотра и создания объекта не меняем логику,
                                                                # но право вносить изменения PATCH... /ЗАПРОСЫ с идентификатором/ даем только автору
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.creator
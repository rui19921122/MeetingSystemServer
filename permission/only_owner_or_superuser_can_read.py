from rest_framework.permissions import BasePermission


class OnlyOwnerOrSuperuserCanReadAndEdit(BasePermission):
    message = "无权限"

    def has_object_permission(self, request, view, obj):
        """
        :param obj:
        :param view:
        :type request:django.http.request.HttpRequest
        :return:
        """
        if request.user.is_superuser:
            return True
        if request.user.user.department == obj.department:
            return True
        else:
            return False

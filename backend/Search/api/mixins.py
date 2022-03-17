from rest_framework import  permissions
from .permissions import EditPermission

class EditPermissionMixin():
    permission_classes = [permissions.IsAdminUser,EditPermission]



class UserQuerySetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)
        
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        return query.filter(**lookup_data)

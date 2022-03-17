from rest_framework import  permissions
from .permissions import EditPermission

class EditPermissionMixin():
    permission_classes = [permissions.IsAdminUser,EditPermission]
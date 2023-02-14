from rest_framework import permissions
from .permissions import IsEditPermissions

class EditPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsEditPermissions]
from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffPermissionMixin():
    permission_classes = [permissions.IsAdminUser,
                           IsStaffEditorPermission
                          ]
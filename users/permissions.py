from rest_framework.permissions import BasePermission

class IsCooperative(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == 'cooperative'

class IsFarmer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == 'farmer'

class IsMachineSupplier(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == 'machine_supplier'

class IsExtensionOfficer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == 'extension_officer'
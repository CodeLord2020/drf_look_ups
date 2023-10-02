from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from .models import Product, student, Account
from .mixins import StaffPermissionMixin
from .serializers import studentSerializer, productSerializer, AccountSerializer, AccountListSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'

class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    lookup_field = 'pk'

class MyCustomViewSet(StaffPermissionMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication] 
    queryset = Product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class CustomUpdateViewSet(StaffPermissionMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication] 
    queryset = Product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'


class AccountViewset(StaffPermissionMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet
                     ):
    authentication_classes = [SessionAuthentication]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'pk'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AccountListSerializer
        else:
            return AccountSerializer
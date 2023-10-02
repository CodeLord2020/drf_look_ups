from django.shortcuts import render
from rest_framework import generics, authentication, filters, mixins, viewsets, serializers

# Create your views here.
from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import studentSerializer, productSerializer, AccountHyperLink
from drfapp.serializers import AccountSerializer, AccountListSerializer,MoneySeializer , AccountDetailSerializer
from drfapp.models import student , Product, Account, Money
from drfapp.authentication import TokenAuthentication, SessionAuthentication
#from rest_framework.authentication import SessionAuthentication 
from .permissions import IsStaffEditorPermission
from .mixins import StaffPermissionMixin
from .pagination import myPagination


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def getdata(request):
    qs = student.objects.all() 
    serializer = studentSerializer(qs, many = True)
    return Response(serializer.data) 

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def getdata_id(request, pk):
    qs = student.objects.get(id=pk) 
    serializer = studentSerializer(qs, many = False)
    return Response(serializer.data)    
    
@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def postdata(request):
    serializer = studentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        instance = serializer.validated_data
        return Response(instance, status = 200)
    return Response({"Error":"data format not applicable"}, status = 400)

from django_filters.rest_framework import DjangoFilterBackend   



class productListCreateView(StaffPermissionMixin,
                            generics.ListCreateAPIView):
    # def get_queryset(self):
    #     return Product.objects.filter(discount='True')
    # def get_queryset(self):
    #     return Product.objects.filter(discount=self.kwargs["discount"])
    
    queryset = Product.objects.all()
    serializer_class = productSerializer
    authentication_classes =[authentication.SessionAuthentication,
                             TokenAuthentication]
    filter_backends = (filters.OrderingFilter,)

    def perform_create(self, serializer):
        user = self.request.user
        category = serializer.validated_data.get('category') or None
        if category is None:
            category = 'artifact'
        serializer.save(user = user)
 
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        request = self.request
        # print(request.user)
        return qs.filter(category = 'artifact')
productLCV = productListCreateView.as_view()






class productUpdateView(StaffPermissionMixin,
                        generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'
    authentication_classes =[authentication.SessionAuthentication]
productUV = productUpdateView.as_view()

class productDetailView(StaffPermissionMixin,
                        generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'
    authentication_classes =[authentication.SessionAuthentication]
pDV = productDetailView.as_view()

class MyCustomAPIView(StaffPermissionMixin,
                      mixins.ListModelMixin, 
                      mixins.CreateModelMixin, 
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, 
                      generics.GenericAPIView):
    queryset = Product.objects.all().order_by("id")
    authentication_classes =[authentication.SessionAuthentication] 
    serializer_class = productSerializer
    pagination_class = myPagination
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
MCAPIVIEW = MyCustomAPIView.as_view()

class productDeleteView(StaffPermissionMixin,
                        generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'
    authentication_classes =[authentication.SessionAuthentication]
productDV = productDeleteView.as_view()



class AccountRetrieveDestroy(StaffPermissionMixin,
                            generics.RetrieveUpdateDestroyAPIView,
                            generics.RetrieveAPIView
                     ):
    authentication_classes = [SessionAuthentication]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'pk'
   
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['instance'] = self.get_object()
        return context

class AccountViewset(StaffPermissionMixin,
                           generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
@api_view(['GET' , 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def putdata(request, pk):
    qs = Account.objects.get(id = pk)
    serializer = AccountSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        instance = serializer.validated_data
        return Response(instance, status = 200)
    return Response({"Error":"data format not applicable"}, status = 400)

class AccountViewLSet(StaffPermissionMixin,
                      viewsets.ModelViewSet):
    queryset = Account.objects.all()
    lookup_field = 'pk'
    authentication_classes= [SessionAuthentication]


    def get_serializer_class(self):
        if self.action == 'list':
            return AccountListSerializer
        else:
            return AccountDetailSerializer


class AccountHyperLink(StaffPermissionMixin,
                      generics.ListCreateAPIView):
    queryset = Account.objects.all()
    lookup_field = 'pk'
    authentication_classes= [SessionAuthentication]
    serializer_class = AccountHyperLink 

class MoneyHyperLink(StaffPermissionMixin,
                      generics.RetrieveUpdateAPIView):
    queryset = Money.objects.all()
    lookup_field = 'pk'
    authentication_classes= [SessionAuthentication]
    serializer_class = MoneySeializer


@api_view(['GET' , 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def Moneyputdata(request, pk):
    qs = Money.objects.get(id = pk)
    serializer = MoneySeializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        instance = serializer.validated_data
        return Response(instance, status = 200)
    return Response({"Error":"data format not applicable"}, status = 400)
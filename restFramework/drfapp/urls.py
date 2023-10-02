from django.urls import path
from .routers import router
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.getdata, name = 'getdata'),
    path('getdata/', views.getdata, name = 'getdata'),
    path('getdata/<int:pk>/', views.getdata_id, name = 'getdata_id'),
    path('postdata/', views.postdata, name = 'postdata'),
    path('products/', views.productLCV),
    path('pproducts/', views.MCAPIVIEW),
    path('products/<int:pk>/detail/', views.pDV, name="product-detail"),
    path('products/<int:pk>/update/', views.productUV, name="update-product"), 
    path('account-list/', views.AccountViewset.as_view(), name = "account-list"),
    path('account/details/<int:pk>/', views.AccountViewLSet.as_view({'get': 'retrieve'}), name='account-detail-url-router'),
    #path('account-list-url/', views.AccountViewLSet.as_view({'get': 'list'}), name='account-list-url'),
    path('account-list/<int:pk>/details/', views.AccountRetrieveDestroy.as_view(), name = "account-detail"),
    path('account-list/<int:pk>/update/', views.putdata, name = "account-update"),
    path('token/', obtain_auth_token),
    path('accounthyper/', views.AccountHyperLink.as_view(), name = 'accounthyper'), 
    path('accounthyper/<int:pk>/', views.MoneyHyperLink.as_view(), name = 'accounthyperdetail'),
    #path('accounthyperdetail/<int:pk>/', views.Moneyputdata, name = 'accounthyperdetail')
]

urlpatterns += router.urls

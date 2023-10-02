from rest_framework.routers import DefaultRouter

from drfapp.viewsets import ProductViewSet, StudentViewSet, MyCustomViewSet, CustomUpdateViewSet, AccountViewset

router = DefaultRouter()
router.register("product_123", ProductViewSet, basename="products")
router.register("students", StudentViewSet, basename="students")
router.register("productss", MyCustomViewSet, basename="productss")
router.register("update", CustomUpdateViewSet, basename = "update-product")
router.register('account-list', AccountViewset, basename = "account-detail-url-router")
#router.register('account-list/<int:pk>/edit', AccountDetailViewset, basename = "accounts-details")
#print(router.urls)
urlpatterns = router.urls






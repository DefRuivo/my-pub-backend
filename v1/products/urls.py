from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductSingleSet

app_name = "products"

router = DefaultRouter()

router.register(
    r"",
    ProductViewSet,
    basename="products",
)
router.register(
    r"/(?P<product_id>\d+)",
    ProductSingleSet,
    basename="products-single",
)

urlpatterns = router.urls

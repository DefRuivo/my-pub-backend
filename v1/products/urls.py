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
    r"/(?P<brand_id>\d+)",
    ProductSingleSet,
    basename="products_single",
)

urlpatterns = router.urls

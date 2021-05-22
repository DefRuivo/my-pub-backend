from rest_framework.routers import DefaultRouter

from .views import ProductItemViewSet, ProductItemSingleSet

app_name = "product_items"

router = DefaultRouter()

router.register(
    r"",
    ProductItemViewSet,
    basename="product-items",
)
router.register(
    r"/(?P<item_id>\d+)",
    ProductItemSingleSet,
    basename="product-items-single",
)

urlpatterns = router.urls

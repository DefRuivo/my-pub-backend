from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, BrandSingleSet

app_name = "brands"

router = DefaultRouter()
router.register(
    r"",
    BrandViewSet,
    basename="brands",
)
router.register(
    r"/(?P<brand_id>\d+)",
    BrandSingleSet,
    basename="brands_single",
)
urlpatterns = router.urls

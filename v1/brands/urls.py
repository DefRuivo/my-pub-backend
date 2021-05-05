from rest_framework.routers import DefaultRouter

from .views import BrandViewSet

app_name = "brands"

router = DefaultRouter()
router.register(r"", BrandViewSet, basename="brands")

urlpatterns = router.urls

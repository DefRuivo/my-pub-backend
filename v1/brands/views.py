from .serializers import BrandSerializer
from core.models import Brand
from v1.utils import BaseViewSet, BaseSingleSet


class BrandViewSet(BaseViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all().order_by("name")


class BrandSingleSet(BaseSingleSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.filter()

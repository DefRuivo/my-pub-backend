from .serializers import ProductSerializer
from core.models import Product
from v1.utils import BaseViewSet, BaseSingleSet


class ProductViewSet(BaseViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("name")


class ProductSingleSet(BaseSingleSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()

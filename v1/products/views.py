from .serializers import ProductSerializer
from core.models import Product
from v1.utils import BaseViewSet, BaseSingleSet


class ProductViewSet(BaseViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        params = {}

        brand = self.request.query_params.get("brand")
        if brand:
            params["brand_id"] = brand

        return Product.objects.filter(**params).order_by("name")


class ProductSingleSet(BaseSingleSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()

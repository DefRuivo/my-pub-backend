from .serializers import ProductItemSerializer
from core.models import ProductItem
from v1.utils import BaseViewSet, BaseSingleSet


class ProductItemViewSet(BaseViewSet):
    serializer_class = ProductItemSerializer

    def get_queryset(self):
        params = {}

        product = self.request.query_params.get("product")
        if product:
            params["product_id"] = product

        return ProductItem.objects.filter(**params).order_by("id")


class ProductItemSingleSet(BaseSingleSet):
    serializer_class = ProductItemSerializer
    queryset = ProductItem.objects

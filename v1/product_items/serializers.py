from rest_framework import serializers

from core.models import ProductItem


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = (
            "id",
            "product",
            "created_at",
            "updated_at",
            "quantity",
            "bought_in",
            "valid_until",
            "batch",
        )
        read_only_fields = ("id", "created_at", "updated_at")

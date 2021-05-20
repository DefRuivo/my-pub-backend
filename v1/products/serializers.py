from rest_framework import serializers

from core.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "created_at",
            "updated_at",
            "image",
            "category",
            "brand",
            "name",
            "barcode",
            "description",
            "quantity",
            "quantity_unit",
        )
        read_only_fields = ("id", "created_at", "updated_at")

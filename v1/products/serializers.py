from rest_framework import serializers

from core.models import Product, ProductItem


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
        read_only_fields = ("id", "created_at", "updated_at", "product")

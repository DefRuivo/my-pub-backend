from rest_framework import serializers

from core.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "created_at",
            "updated_at",
            "name",
            "website",
            "facebook",
            "twitter",
            "linkedin",
        )
        read_only_fields = ("id", "created_at", "updated_at")

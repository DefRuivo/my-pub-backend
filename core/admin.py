from django.contrib import admin

from internal.models import ImprovedModelAdmin

from .models import User, Brand, Product, ProductItem


@admin.register(User)
class UserAdmin(ImprovedModelAdmin):
    def show_groups(self, obj):
        groups = []
        for group in obj.groups.all():
            groups.append(group.name)
        return ",".join(groups)

    search_fields = ("id", "email", "first_name", "last_name")
    list_display = (
        "id",
        "is_active",
        "email",
        "first_name",
        "last_name",
        "show_groups",
    )


@admin.register(Brand)
class BrandAdmin(ImprovedModelAdmin):
    search_fields = ("id", "name")
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(ImprovedModelAdmin):
    search_fields = ("id", "name", "barcode")
    list_display = (
        "id",
        "name",
        "brand",
        "category",
        "barcode",
        "quantity",
        "quantity_unit",
    )
    list_filter = ("category",)


@admin.register(ProductItem)
class ProductItemAdmin(ImprovedModelAdmin):
    list_display = (
        "id",
        "quantity",
        "bought_in",
        "valid_until",
        "batch",
        "product",
    )

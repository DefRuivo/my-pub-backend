from django.urls import include, path
from django.conf import settings

app_name = "v1"

urlpatterns = [
    path("users/", include("v1.users.urls")),
    path("brands/", include("v1.brands.urls")),
    path("products/", include("v1.products.urls")),
    path("product_items/", include("v1.product_items.urls")),
]

if settings.DEBUG is True:
    urlpatterns.append(path("debug/", include("v1.debug.urls")))

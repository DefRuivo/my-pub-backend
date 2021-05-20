from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("users/", include("v1.users.urls")),
    path("brands/", include("v1.brands.urls")),
    path("products/", include("v1.products.urls")),
]

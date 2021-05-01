from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views


urlpatterns = [
    path("auth", views.obtain_auth_token),
    path("v1/", include("v1.urls")),
    path("admin/", admin.site.urls),
]

from django.urls import path

from .views import TearDownView, SetUpView

app_name = "debug"

urlpatterns = [
    path("teardown", TearDownView.as_view(), name="teardown"),
    path("setup", SetUpView.as_view(), name="setup"),
]

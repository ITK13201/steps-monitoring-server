from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path("", include("backend.home.urls")),
    path("api/", include("backend.api.urls")),
]

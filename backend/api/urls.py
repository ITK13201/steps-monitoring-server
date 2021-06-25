from django.urls import path
from django.urls.conf import include


urlpatterns = [path("steps/", include("backend.api.steps.urls"))]

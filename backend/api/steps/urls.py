from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [path("add/", views.StepAddAPIView.as_view(), name="api_steps_add")]

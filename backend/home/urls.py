from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("media/figure.svg", views.plot_figure_view, name="media_figure"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name = "book")
]
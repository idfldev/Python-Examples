from django.urls import path
from application_forms import views

urlpatterns = [
    path("", views.home, name="home"),
]
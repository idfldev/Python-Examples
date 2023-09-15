from django.urls import path, include
from Inspector import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf/', views.pdfPage, name='pdf-page'),
]

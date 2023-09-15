from django.urls import path
from . import views

urlpatterns = [
    # ==== path Converters ====
    # int: numbers
    # str: strings
    # path: whole url / 
    # slug: hyphen-and_underscore_stuff
    # UUID: universally unique identifier
    # path('<int:year>/<str:month>', views.home, name='home'),
    path('', views.home, name='home'),
    path('testing/', views.testing, name='testing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('audit/', views.audit, name='audit'),
    path('application-form/', views.application_form, name='application-form'),
    
]
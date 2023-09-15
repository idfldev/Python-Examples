
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("application_forms.urls"), name='home'),
    path('login/', include("users.urls"), name='login'),
    path('logout/', include("users.urls"), name='logout'),
]

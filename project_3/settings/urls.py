
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import LoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', include('login.urls')),
    path('login/', include('staff.urls')),
    path('', include('Application_form.urls')),
    path('idfl/', include('staff.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
admin.site.site_header = 'IDFL Vietnam System'
admin.site.site_title = 'Browser Title'
admin.site.index_title = 'Welcome IDFL Vietnam Administration'
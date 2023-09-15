
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('staff/', include('django.contrib.auth.urls')),
    path('staff/', include('staff.urls')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'IDFL Vietnam System'
admin.site.site_title = 'Browser Title'
admin.site.index_title = 'Welcome IDFL Vietnam Administration'

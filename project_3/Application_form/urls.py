from django.urls import path
from . import views
from myModules.randomID import generateIdForm



# form_id_url = "blog-admin"

FORM_ID_URL = generateIdForm("n")
print(FORM_ID_URL)

urlpatterns = [
    # ==== path Converters ===={form_id_url}/
    # int: numbers
    # str: strings
    # path: whole url / 
    # slug: hyphen-and_underscore_stuff
    # UUID: universally unique identifier
    # path('<int:year>/<str:month>', views.home, name='home'),
    path('', views.home, name='home'),
    # path('GRS_RCS/', views.grsRcs, name='grs-rcs'),
    path(f'{FORM_ID_URL}/', views.grsRcs, name='grs-rcs'),
    # path('audit/', views.homeAudit, name='home-audit'),
    # path('application-form/', views.application_form, name='application-form'),
    
]
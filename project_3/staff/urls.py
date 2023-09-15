from django.urls import path, include
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # ==== path Converters ====
    # int: numbers
    # str: strings
    # path: whole url / 
    # slug: hyphen-and_underscore_stuff
    # UUID: universally unique identifier
    # path('<int:year>/<str:month>', views.home, name='home'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.registerPage, name='register-page'),
    path('login/', views.loginPage, name='login-page'),
    # path('logout/', views.logoutPage, name='logout-page'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout-page'),


    path('', views.dashboard, name='dashboard'),
    path('auditor/', views.audit, name='auditor'),
    path('cs/', views.cs, name='cs'),
    path('inspector/', views.inspection, name='inspector'),
    path('task/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task-detail'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]
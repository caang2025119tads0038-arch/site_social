from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # url de login antiga
    # path('login/', views.user_login, name='login'),

    # urls de login e logout pardão
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
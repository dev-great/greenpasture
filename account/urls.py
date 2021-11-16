from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



app_name = 'account'

urlpatterns = [
    path('login/', views.login_view , name='login_view'),
    path('register/', views.register_view , name='register_view'),
    path('logout/', views.logout , name='logout'),
    path('password_reset_request/', views.password_reset_request , name='password_reset_request'),
]

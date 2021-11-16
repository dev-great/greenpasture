from django.urls import path
from . import views
from .views import stores, store_listing

app_name = 'store'

urlpatterns = [
    path('store/', views.stores , name='store'),

]

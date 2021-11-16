from django.urls import path
from . import views
from about.views import about

app_name = 'about'

urlpatterns = [
path('about/', about, name="about"),
]
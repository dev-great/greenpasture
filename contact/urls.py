from django.urls import path
from . import views
from contact.views import contact_us, thanks

app_name = 'contact'

urlpatterns = [
path('contact/', contact_us, name="contact_us"),
path('thanks/', thanks, name='thanks'),
]
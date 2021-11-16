from django.shortcuts import render
from django.contrib import messages,auth
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView, ListView
from home.models import Livestream

# Create your views here.
class home(ListView):
   model = Livestream
   template_name = 'home/index.html'
   context_object_name = 'Livestream'

   def get_context_data(self, *args, **kwargs):
      context = super(home, self).get_context_data(*args, **kwargs)
      return context
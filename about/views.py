from django.shortcuts import render
from django.contrib import messages,auth
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

def about(request):
    return render(request, 'about/about.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Division  # Corrected import path

# Create your views here.

def dashboard(request):
    return render(request, 'base.html')

def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html', {'divisions': divisions})

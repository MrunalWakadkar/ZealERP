from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    return render(request, 'base.html')


from django.shortcuts import render
from studentApp.models import Course



def dashboard(request):
    return render(request, 'base.html')


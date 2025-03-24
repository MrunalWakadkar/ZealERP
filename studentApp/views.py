from django.shortcuts import render
from studentApp.models import Course, Division



def dashboard(request):
    return render(request, 'base.html')

def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html', {'divisions': divisions})

def courses(request):
    courses = Course.objects.all()
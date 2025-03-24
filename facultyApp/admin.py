from django.contrib import admin
from facultyApp.models import Division

# Register your models here.
from .models import Staff

admin.site.register(Staff)

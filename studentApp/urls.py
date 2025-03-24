from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('',views.courses,name='courses'),
    path('',views.divisions,name='divisions'),
]
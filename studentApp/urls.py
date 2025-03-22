from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('view_subjects', views.view_subjects, name = 'view_subjects'),
]
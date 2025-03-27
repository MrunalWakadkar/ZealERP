from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('profile' , views.profile ,name="profile"),
    path('update_profile' , views.update_profile ,name="update_profile"),
    path('change_password' , views.change_pass ,name="change_password"),

    path('view_subjects', views.view_subjects, name = 'view_subjects'),

    path('',views.courses,name='courses'),
    path('manage-division',views.divisions,name='divisions'),

]
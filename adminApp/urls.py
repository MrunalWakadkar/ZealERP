from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('', views.dashboard, name='dashboard'),
    path('manage-course', views.courses, name='courses'),
    path('manage-division', views.divisions, name='divisions'),
    path('add_division', views.add_division, name='divisions'),

    path('edit-division/<int:division_id>/', views.edit_division, name='edit_division'),
    path('delete-division/<int:division_id>/', views.delete_division, name='delete_division'),

    path('manage-course', views.courses, name='manage_course'),
    path('edit-course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('add-course/', views.add_course, name='add_course'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
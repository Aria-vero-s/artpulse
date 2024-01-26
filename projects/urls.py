from django.urls import path
from . import views

urlpatterns = [
    path('create_project/', views.create_project, name='create_project'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('<int:project_id>/interested/', views.interested_toggle, name='interested_toggle'),
    path('update_project/<int:project_id>/', views.update_project, name='update_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
]

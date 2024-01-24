from django.urls import path
from .views import create_project, project_detail, interested_toggle

urlpatterns = [
    path('create_project/', create_project, name='create_project'),
    path('<int:project_id>/', project_detail, name='project_detail'),
    path('<int:project_id>/interested/', interested_toggle, name='interested_toggle'),
]

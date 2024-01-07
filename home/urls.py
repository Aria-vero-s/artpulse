from django.urls import path
from . import views
from .views import index, rate_artwork, add_comment, create_artwork, update_artwork, delete_artwork

urlpatterns = [
    path('', views.index, name='index'),
    path('rate/<int:artwork_id>/', rate_artwork, name='rate_artwork'),
    path('comment/<int:artwork_id>/', add_comment, name='add_comment'),
    path('create/', create_artwork, name='create_artwork'),
    path('update/<int:artwork_id>/', update_artwork, name='update_artwork'),
    path('delete/<int:artwork_id>/', delete_artwork, name='delete_artwork'),
]

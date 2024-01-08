from django.urls import path
from . import views
from .views import index, account, ChangeProfilePictureView, create_artwork, delete_artwork_list, delete_artwork, update_artwork_list, update_artwork, rate_artwork, add_comment, search_artworks

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('change_profile_picture/', ChangeProfilePictureView.as_view(), name='change_profile_picture'),
    path('search/', search_artworks, name='search_artworks'),
    path('rate/<int:artwork_id>/', rate_artwork, name='rate_artwork'),
    path('comment/<int:artwork_id>/', add_comment, name='add_comment'),
    path('create/', create_artwork, name='create_artwork'),
    path('update/<int:artwork_id>/', update_artwork, name='update_artwork'),
    path('delete/<int:artwork_id>/', delete_artwork, name='delete_artwork'),
    path('delete/', delete_artwork_list, name='delete_artwork_list'),
    path('update/', update_artwork_list, name='update_artwork_list'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error/', views.error, name='error'),
    path('account/', views.account, name='account'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('account_deleted/', views.account_deleted, name='account_deleted'),
    path('change_profile_picture/', views.ChangeProfilePictureView.as_view(), name='change_profile_picture'),
    path('search/', views.search_artworks, name='search_artworks'),
    path('rate/<int:artwork_id>/', views.rate_artwork, name='rate_artwork'),
    path('comment/<int:artwork_id>/', views.add_comment, name='add_comment'),
    path('create/', views.create_artwork, name='create_artwork'),
    path('update/<int:artwork_id>/', views.update_artwork, name='update_artwork'),
    path('delete/<int:artwork_id>/', views.delete_artwork, name='delete_artwork'),
    path('artwork/<int:artwork_id>/', views.ArtworkDetailView.as_view(), name='artwork_detail'),
    path('contact_form/', views.contact_form, name='contact_form'),
    path('like/<int:artwork_id>/', views.like_artwork, name='like_artwork'),
]
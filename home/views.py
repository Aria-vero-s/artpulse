from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artwork, Comment, UserProfile, Like
from projects.models import CollaborativeProject
from .forms import RatingForm, CommentForm, ArtworkForm
from django.db.models import Q, Count, Avg
from django.utils.decorators import method_decorator
from django.views import View
from .forms import ProfilePictureForm
from allauth.account.views import LogoutView
from django.contrib.auth.models import User
from allauth.account.adapter import get_adapter
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout


def index(request):
    artworks = Artwork.objects.all()
    return render(request, 'index.html', {'artworks': artworks})


def error(request):
    return render(request, 'error.html', {})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    
    artworks = Artwork.objects.filter(artist=user)
    total_artworks = artworks.count()
    average_rating = artworks.aggregate(avg_rating=Avg('rating'))['avg_rating']
    total_critiques = artworks.filter(comments__isnull=False).count()

    collaborative_projects = CollaborativeProject.objects.filter(user=user_profile.user)

    context = {
        'user_profile': user_profile,
        'artworks': artworks,
        'collaborative_projects': collaborative_projects,
        'total_artworks': total_artworks,
        'average_rating': average_rating,
        'total_critiques': total_critiques,
    }

    return render(request, 'user_profile.html', context)


def account(request):
    collaborative_projects = CollaborativeProject.objects.filter(user=request.user)
    artworks = Artwork.objects.all()

    user_profile = UserProfile.objects.get(user=request.user)
    artworks = Artwork.objects.filter(artist=request.user)

    total_artworks = artworks.count()
    average_rating = artworks.aggregate(avg_rating=Avg('rating'))['avg_rating']
    total_critiques = artworks.filter(comments__isnull=False).count()

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'artworks': artworks,
        'total_artworks': total_artworks,
        'average_rating': average_rating,
        'total_critiques': total_critiques,
        'collaborative_projects': collaborative_projects,
    }

    return render(request, 'account.html', context)


@method_decorator(login_required, name='dispatch')
class ChangeProfilePictureView(View):
    template_name = 'change_profile_picture.html'

    def get(self, request, *args, **kwargs):
        form = ProfilePictureForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid():
            form.save()
            return redirect('account')

        return render(request, self.template_name, {'form': form})


def rate_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            artwork.rating = (artwork.rating + rating) / 2
            artwork.save()

    return redirect('artwork_detail', artwork_id=artwork_id)


def add_comment(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment_text = form.cleaned_data['comment']
                Comment.objects.create(artwork=artwork, user=request.user, text=comment_text)
                messages.success(request, 'Comment added successfully!')
            else:
                messages.error(request, 'Failed to add comment. Please check your input.')
        else:
            messages.info(request, 'You need to sign up first to write a comment!')
            return redirect('account_signup')

    return redirect('artwork_detail', artwork_id=artwork_id)

@login_required
def create_artwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user
            artwork.save()
            return redirect('account')
    else:
        form = ArtworkForm()

    return render(request, 'create_artwork.html', {'form': form})


@login_required
def delete_artwork(request, artwork_id):
    artwork = Artwork.objects.get(pk=artwork_id)
    if request.method == 'POST':
        artwork.delete()
        return redirect('account')
    return render(request, 'delete_artwork.html', {'artwork': artwork})


@login_required
def update_artwork(request, artwork_id):
    artwork = Artwork.objects.get(pk=artwork_id)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = ArtworkForm(instance=artwork)

    return render(request, 'update_artwork.html', {'form': form, 'artwork': artwork})


def search_artworks(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    rating = request.GET.get('rating', '')

    print(f"Query: {query}, Rating: {rating}")

    artworks = Artwork.objects.all()
    
    if query:
        artworks = Artwork.objects.filter(
            Q(title__icontains=query) | 
            Q(artist__username__icontains=query) | 
            Q(description__icontains=query)
        )
    if category:
        artworks = artworks.filter(category=category)
    if rating:
        rating = float(rating)
        artworks = artworks.filter(rating__gte=rating)

    return render(request, 'index.html', {'artworks': artworks, 'query': query, 'category': category, 'rating': rating})


@login_required
def delete_account(request):
    if request.method == 'POST':
        # Deactivate the user account
        user = request.user
        user.is_active = False
        user.save()

        # Log the user out
        logout(request)

        # Redirect to a confirmation page or any other appropriate view
        messages.success(request, 'Your account has been successfully deleted.')
        return redirect('index')

    return render(request, 'delete_account.html')


def account_deleted(request):
    return render(request, 'account_deleted.html', {})


class ArtworkDetailView(View):
    def get(self, request, artwork_id):
        artwork = get_object_or_404(Artwork, pk=artwork_id)
        return render(request, 'artwork_detail.html', {'artwork': artwork})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('contact_form')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})


@login_required
def like_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)

    if not request.user.is_authenticated:
        messages.error(request, 'You must log in first.')

    if request.user in artwork.likes.all():
        # User has already liked, remove the like
        artwork.likes.remove(request.user)
        liked = False
    else:
        # User hasn't liked, add the like
        artwork.likes.add(request.user)
        liked = True

    like_count = artwork.likes.count()

    response_data = {
        'liked': liked,
        'like_count': like_count,
    }

    return JsonResponse(response_data)
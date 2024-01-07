from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artwork, Comment
from .forms import RatingForm, CommentForm, ArtworkForm


def index(request):
    artworks = Artwork.objects.all()
    return render(request, 'index.html', {'artworks': artworks})

def rate_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            artwork.rating = (artwork.rating + rating) / 2
            artwork.save()

    return redirect('index')

def add_comment(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment']
            Comment.objects.create(artwork=artwork, user=request.user, text=comment_text)

    return redirect('index')

@login_required
def create_artwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user
            artwork.save()
            return redirect('index')
    else:
        form = ArtworkForm()

    return render(request, 'create_artwork.html', {'form': form})

@login_required
def update_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id, artist=request.user)

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArtworkForm(instance=artwork)

    return render(request, 'update_artwork.html', {'form': form, 'artwork': artwork})

@login_required
def delete_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id, artist=request.user)

    if request.method == 'POST':
        artwork.delete()
        return redirect('index')

    return render(request, 'delete_artwork.html', {'artwork': artwork})
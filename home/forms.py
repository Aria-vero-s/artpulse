from django import forms
from .models import Artwork, UserProfile

class RatingForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5)

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'image', 'category']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

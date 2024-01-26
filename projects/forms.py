from django import forms
from .models import CollaborativeProject


class CollaborativeProjectForm(forms.ModelForm):
    class Meta:
        model = CollaborativeProject
        fields = ['title', 'description']

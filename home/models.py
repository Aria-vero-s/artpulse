from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Artwork(models.Model):
    CATEGORY_CHOICES = [
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
        ('digital_art', 'Digital Art'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    artwork = models.ForeignKey(Artwork, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.artwork.title}'

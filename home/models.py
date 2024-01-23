from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField('profile_picture', upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


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


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

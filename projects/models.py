from django.db import models
from django.contrib.auth.models import User

class CollaborativeProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    interested_users = models.ManyToManyField(User, related_name='interested_projects', blank=True)

    def __str__(self):
        return self.title

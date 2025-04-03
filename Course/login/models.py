from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    github_url = models.URLField(blank=True)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
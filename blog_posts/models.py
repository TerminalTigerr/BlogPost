from django.db import models

class Author(models.Model):
    """Information about the author"""
    user = models.TextField()
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog', null=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_user', blank=True)
    bookmark_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark_user', blank=True)
    def __str__(self):
        return self.title
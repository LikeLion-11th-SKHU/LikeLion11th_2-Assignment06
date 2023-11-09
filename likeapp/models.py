from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='blogs')
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_blogs')
    bookmark_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='bookmark_user')

    def __str__(self):
        return self.title
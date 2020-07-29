from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'post_images', blank = True)
    URL = models.URLField(max_length=200,blank= True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
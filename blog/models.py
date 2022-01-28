from datetime import timezone
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # image
    image = models.ImageField(default='default.png', upload_to='article_images')
    body = RichTextUploadingField(blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    # time
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
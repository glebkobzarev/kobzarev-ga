from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
<<<<<<< HEAD


=======
>>>>>>> 761f8fac9ce22fdea80e4ba390301800017b8f42
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
 .filter(status=Post.Status.PUBLISHED)
<<<<<<< HEAD
    
class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
     
=======

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
>>>>>>> 761f8fac9ce22fdea80e4ba390301800017b8f42
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
    on_delete=models.CASCADE,
    related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
    choices=Status.choices,
    default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
<<<<<<< HEAD
 
class Meta:
 ordering = ['-publish']
 indexes = [
 models.Index(fields=['-publish']),
 ]
 def __str__(self):
    return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']
        indexes = [
        models.Index(fields=['created']),
        ]
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

 
=======

class Meta:
    ordering = ['-publish']
    indexes = [
 models.Index(fields=['-publish']),
 ]
    def __str__(self):
        return self.title
>>>>>>> 761f8fac9ce22fdea80e4ba390301800017b8f42

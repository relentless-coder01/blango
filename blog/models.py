from django.db import models
from django.conf import settings
# Create your models here.

class Tag(models.Model):
  value = models.TextField(max_length=100, unique=True)
  class Meta:
    ordering = ["value"]
  def __str__(self):
    return self.value

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  published_at = models.DateTimeField(blank=True, null=True, db_index=True)
  title = models.TextField(max_length=100)
  slug = models.SlugField(unique=True)
  summary = models.TextField(max_length=500)
  content = models.TextField()
  tags = models.ManyToManyField(Tag, related_name="posts")

  def __str__(self):
    return self.title

class Comment(models.Model):
  creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

  def __str__(self):
        return self.creator.__str__()
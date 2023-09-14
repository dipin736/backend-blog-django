from django.db import models
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    short_description = models.TextField(max_length=3000)
    published_on = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='images')  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
   

class Comment(models.Model):
    name = models.CharField(max_length=40)
    body = models.CharField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments', related_query_name='comment')
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.name)


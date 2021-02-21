from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    """ Create Post Date Base """

    title = models.CharField(
        max_length=250,
    )
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    body = RichTextField(max_length=5000)
    overview = models.CharField(
        max_length=350,
    )
    author = models.ForeignKey(
        User, related_name="blog_posts", on_delete=models.CASCADE
    )
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog_photos/")

    """ ordering by newest  Post """

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(
        max_length=250,
    )
    email = models.EmailField()
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"

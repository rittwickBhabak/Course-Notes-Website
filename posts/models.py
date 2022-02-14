from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=300)
    tags = TaggableManager(blank=True)

    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    edited_at = models.DateField(auto_now=True)

    def get_next(self):
        next = Post.objects.filter(pk__gt=self.pk)
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Post.objects.filter(pk__lt=self.pk).order_by('-pk')
        if prev:
            return prev.first()
        return False

    def get_absolute_url(self):
        return reverse("posts:view-post", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title 

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('socialmedia:blog_detail', kwargs={'slug': self.slug})

class SocialMediaLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

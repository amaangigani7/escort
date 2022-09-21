from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image_link = models.CharField(max_length=2000, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        try:
            return self.title
        except:
            return "No Title"


class LoveStory(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    image_link = models.CharField(max_length=2000, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']
        verbose_name_plural = "LoveStories"

    def __str__(self):
        try:
            return self.title
        except:
            return "No Title"

class Subscriber(models.Model):
    email = models.EmailField(null=True)

    def __str__(self):
        try:
            return self.email
        except:
            return "None"

class PageData(models.Model):
    title = models.CharField(max_length=255)
    img_link = models.TextField(null=True, blank=True)
    content = models.TextField()
    youtube_link = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Page Data"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# class ContactUs(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
#   # phone = PhoneNumberField()
#     message = models.TextField()
#     sent_on = models.DateTimeField(auto_now_add=True, null=True)

#     class Meta:
#         verbose_name_plural = 'Contact Us'
#         ordering = ['-sent_on']

#     def __str__(self):
#         return self.name + ' - ' + self.email
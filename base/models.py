from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from datetime import date
import os


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


def original_image(instance, filename):
    if instance.original_image  and filename:
        return os.path.join('original_images', filename)
    else:
        return 'images/' + filename


def segmented_image(instance, filename):
    if instance.segmented_image  and filename:
        return os.path.join('segmented_images', filename)
    return 'images/' + filename


def detected_image(instance, filename):
    if instance.detected_image  and filename:
        return os.path.join('detected_images', filename)
    return 'images/' + filename    

class Post(models.Model):

    disease = models.CharField(max_length=255, null=False, blank=False)
    severity = models.IntegerField(null=False, blank=False)
    original_image = models.ImageField(upload_to=original_image, null=False, blank=False)
    detected_image = models.ImageField(upload_to=detected_image, null=False, blank=False)
    segmented_image = models.ImageField(upload_to=segmented_image, null=False, blank=False)
    
    locations = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateField(default=date.today)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    objects = models.Manager()  # default manager
   # custom manager

    class Meta:
        ordering = ('-detected_image',)

    def __str__(self):
        return self.disease







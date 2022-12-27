from django.db import models
from django.conf import settings

# Create your models here.
class Feed(models.Model):
    feedPhotoPath = models.ImageField(upload_to='feeds/%Y/%m/%d/', max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=255)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
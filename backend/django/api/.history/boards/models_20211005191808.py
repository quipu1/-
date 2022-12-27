from django.db import models
from django.conf import settings
from beers.models import Beer

# Create your models here.
class Board(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=3)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)

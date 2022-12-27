from django.db import models
from django.conf import settings


class Type(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Beer(models.Model):
    beer_kor_name = models.CharField(max_length=255, blank=True, null=True)
    beer_eng_name = models.CharField(max_length=255, blank=True, null=True)
    beerPhotoPath = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    beer_type = models.CharField(max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    score = models.FloatField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    aroma = models.FloatField(blank=True, null=True)
    appearance = models.FloatField(blank=True, null=True)
    flavor = models.FloatField(blank=True, null=True)
    mouthfeel = models.FloatField(blank=True, null=True)
    types = models.ManyToManyField(Type)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, 
        related_name='like_beers', 
        through='Like',
    )


class Like(models.Model):
    beer = models.ForeignKey('Beer', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
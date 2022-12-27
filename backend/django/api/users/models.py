from django.db import models
from django.contrib.auth.models import AbstractUser
from beers.models import Type

# Create your models here.
class User(AbstractUser):
    userID = models.CharField(unique=True, max_length=20, blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    profilePhotoPath = models.ImageField(upload_to='profiles/%Y/%m/%d/', max_length=505, blank=True, null=True)
    gender = models.BooleanField(default=0, null=True)
    age = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    logitude = models.FloatField(blank=True, null=True)
    types = models.ManyToManyField(Type)
    friends = models.ManyToManyField('self')
    add_friends = models.ManyToManyField('self', symmetrical=False, related_name='take_list')



from django.db import models


class Badge(models.Model):
    icon = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    lowcut = models.IntegerField(db_column='lowCut', blank=True, null=True)  # Field name made lowercase.
    highcut = models.IntegerField(db_column='highCut', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'badge'


class Beer(models.Model):
    beer_kor_name = models.CharField(max_length=255, blank=True, null=True)
    beer_eng_name = models.CharField(max_length=255, blank=True, null=True)
    beerphotopath = models.CharField(db_column='beerPhotoPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    score = models.FloatField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    aroma = models.FloatField(blank=True, null=True)
    appearance = models.FloatField(blank=True, null=True)
    flavor = models.FloatField(blank=True, null=True)
    mouthfeel = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beer'


class BeerPredict(models.Model):
    beer = models.ForeignKey(Beer, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    beer_predict = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beer_predict'


class Comment(models.Model):
    content = models.CharField(max_length=255, blank=True, null=True)
    feed = models.ForeignKey('Feed', models.DO_NOTHING, db_column='feed')
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')

    class Meta:
        managed = False
        db_table = 'comment'


class Feed(models.Model):
    feedphotopath = models.CharField(db_column='feedPhotoPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')

    class Meta:
        managed = False
        db_table = 'feed'


class FeedLike(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    feed = models.ForeignKey(Feed, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feed_like'


class Friend(models.Model):
    req_user = models.IntegerField(blank=True, null=True)
    res_user = models.IntegerField(blank=True, null=True)
    allow = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'friend'


class Level(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    lowcut = models.IntegerField(db_column='lowCut', blank=True, null=True)  # Field name made lowercase.
    highcut = models.IntegerField(db_column='highCut', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level'


class Review(models.Model):
    review_score = models.FloatField()
    review_content = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    beer = models.ForeignKey(Beer, models.DO_NOTHING, db_column='beer')
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')

    class Meta:
        managed = False
        db_table = 'review'


class Snack(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True)
    beer = models.ForeignKey(Beer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'snack'


class User(models.Model):
    user_id = models.CharField(unique=True, max_length=20, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    userphotopath = models.CharField(db_column='userPhotoPath', max_length=505, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    logitude = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
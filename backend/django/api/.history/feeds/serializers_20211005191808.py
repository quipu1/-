from rest_framework import serializers
from .models import Feed, Comment


class FeedListSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')

    class Meta:
        model = Feed
        fields = ('id', 'content', 'userID', 'feedPhotoPath', 'created_at')


class FeedSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')

    class Meta:
        model = Feed
        fields = ('id', 'content', 'userID', 'feedPhotoPath', 'created_at')



class CommentListSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')

    class Meta:
        model = Comment
        fields = ('id', 'content', 'feed', 'userID', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'feed', 'userID', 'created_at')
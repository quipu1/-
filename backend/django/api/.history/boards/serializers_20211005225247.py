from rest_framework import serializers
from .models import Board


class BoardListSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')
    nickname = serializers.ReadOnlyField(source='user.nickname')

    class Meta:
        model = Board
        fields = ('id', 'content', 'userID', 'nickname', 'score', 'created_at', 'beer')

class BoardSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')
    nickname = serializers.ReadOnlyField(source='user.nickname')

    class Meta:
        model = Board
        fields = ('id', 'content', 'userID', 'nickname', 'score', 'created_at', 'beer')

class BoardRecommendSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')
    nickname = serializers.ReadOnlyField(source='user.nickname')

    class Meta:
        model = Board
        fields = ('userID', 'nickname', 'score', 'beer')
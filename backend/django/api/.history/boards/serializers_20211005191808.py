from rest_framework import serializers
from .models import Board


class BoardListSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')

    class Meta:
        model = Board
        fields = ('id', 'content', 'userID', 'score', 'created_at', 'beer')

class BoardSerializer(serializers.ModelSerializer):
    userID = serializers.ReadOnlyField(source='user.userID')

    class Meta:
        model = Board
        fields = ('id', 'content', 'userID', 'score', 'created_at', 'beer')

class BoardRecommendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ('nickname', 'score', 'beer')
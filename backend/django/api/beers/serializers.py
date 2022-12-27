from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Beer, Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class BeerListSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True, read_only=True)     
    class Meta:
        model = Beer
        fields = '__all__'


class BeerSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True, read_only=True)

    class Meta:
        model = Beer
        fields = '__all__'
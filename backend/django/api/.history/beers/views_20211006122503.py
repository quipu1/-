from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Beer, Type
from .serializers import (
    BeerSerializer,
    BeerListSerializer,
)
from django.db.models import Q
from django.contrib.auth import (
    get_user_model,
)
from django.db.models import Count
from boards.models import Board


@api_view(['GET'])
def beer_list(request):
    beers = Beer.objects.all()
    serializer = BeerListSerializer(beers, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def beer_list_type(request, type):
    type_info = get_object_or_404(Type, name=type)
    beers = Beer.objects.filter(types=type_info)
    serializer = BeerListSerializer(beers, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def beer_detail(request, beer_id):
    beer = get_object_or_404(Beer, id=beer_id)
    serializer = BeerSerializer(beer)
    return Response(data=serializer.data)


@api_view(['GET'])
def beer_search(request, keyword):
    beers = Beer.objects.filter(Q(beer_kor_name__contains=keyword)|Q(beer_eng_name__contains=keyword))
    serializer = BeerListSerializer(beers, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def like(request, beer_id, userID):
    User = get_user_model()
    user = get_object_or_404(User, userID=userID)
    beer = get_object_or_404(Beer, pk = beer_id)
    if beer.like_users.filter(pk=user.id):
        beer.like_users.remove(user)
    else:
        beer.like_users.add(user)
    return Response({"status":"CREATE"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_like_list(request, userID):
    User = get_user_model()
    user = get_object_or_404(User, userID=userID)
    beers = user.like_beers.all()
    serializer = BeerListSerializer(beers, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def beer_people_like(request):
    beers = Beer.objects.annotate(total=Count('like_users')).order_by('-total')[:6]
    serializer = BeerListSerializer(beers, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def beer_most_review(request):
    beers = Beer.objects.annotate(total=Count('boards')).order_by('-total')[:6] 
    serializer = BeerListSerializer(beers, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
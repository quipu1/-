from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Board
from beers.models import Beer
from .serializers import (
    BoardListSerializer,
    BoardSerializer,

)
from django.contrib.auth import (
    get_user_model,
)
from django.db.models import Q


@api_view(['GET'])
def user_board_list(request, userID):
    User = get_user_model()
    user = get_object_or_404(User, userID = userID)
    boards = Board.objects.filter(user=user).order_by('-pk')
    serializer = BoardListSerializer(boards, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def board_list(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    boards = Board.objects.filter(beer=beer).order_by('-pk')
    serializer = BoardListSerializer(boards, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def board_detail(request, beer_id, board_id):
    board = get_object_or_404(Board, pk=board_id)
    serializer = BoardSerializer(board)
    return Response(data=serializer.data)


@api_view(['POST'])
def board_create(request, beer_id):
    data = request.POST
    beer = get_object_or_404(Beer, pk=beer_id)
    user = get_object_or_404(get_user_model(), userID = data.get('userID'))
    review = Board.objects.get(user = user, beer=beer)
    if review:
        review.delete() 
    if data.get('score'):
        board = Board()
        board.content = data.get('content')
        board.user = user
        board.score = data.get('score')
        board.beer = beer
        board.nickname = user.nickname
        board.save()
        return Response({"status":"CREATE"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status":"NO Score"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def board_update(request, beer_id, board_id):
    data = request.POST
    board = get_object_or_404(Board, pk=board_id)
    print(data.get('content'))
    if data.get('content'):
        board.content = data.get('content')
    if data.get('score'):
        board.score = data.get('score')
    board.save()
    return Response({"status":"UPDATE"}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def board_delete(request, beer_id, board_id):
    board = Board.objects.get(pk=board_id)
    board.delete()
    return Response({"status":"DELETE NO CONTENT"}, status=status.HTTP_204_NO_CONTENT)
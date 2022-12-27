from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Feed, Comment
from .serializers import (
    FeedListSerializer,
    FeedSerializer,
    CommentListSerializer,
    CommentSerializer,
)
from django.contrib.auth import (
    get_user_model,
)

@api_view(['GET'])
def user_feed_list(request, userID):
    User = get_user_model()
    user = get_object_or_404(User, userID = userID)
    feeds = Feed.objects.filter(user = user).order_by('-pk')
    serializer = FeedListSerializer(feeds, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def feed_list(request):
    feeds = Feed.objects.all().order_by('-pk')
    serializer = FeedListSerializer(feeds, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def feed_detail(request, feedID):
    feed = get_object_or_404(Feed, pk=feedID)
    serializer = FeedSerializer(feed)
    return Response(data=serializer.data)


@api_view(['POST'])
def feed_create(request):
    data = request.POST
    print(data)
    if data.get('content'):
        feed = Feed()
        feed.feedPhotoPath = request.FILES['feedPhotoPath']
        feed.content = data.get('content')
        feed.user = get_object_or_404(get_user_model(), userID = data.get('userID'))
        feed.save()
        return Response({"status":"CREATE"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def feed_update(request, feedID):
    data = request.POST
    feed = get_object_or_404(Feed, pk=feedID)
    if data.get('content'):
        feed.content = data.get('content')
    if data.get('feedPhotoPath'):
        feed.feedPhotoPath = data.get('feedPhotoPath')
    feed.save()
    return Response({"status":"UPDATE"}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def feed_delete(request, feedID):
    feed = get_object_or_404(Feed, pk=feedID)
    feed.delete()
    return Response({"status":"DELETE NO CONTENT"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_list(request, feedID):
    feed = get_object_or_404(Feed, pk=feedID)
    comments = Comment.objects.filter(feed=feed)
    serializer = CommentListSerializer(comments, many=True)
    return Response(data=serializer.data)


@api_view(['POST'])
def comment_create(request, feedID):
    data = request.POST
    comment = Comment()
    comment.content = data.get('content')
    comment.user = get_object_or_404(get_user_model(), userID = data.get('userID'))
    comment.feed = get_object_or_404(Feed, pk = feedID)
    comment.save()
    return Response({"status":"CREATE"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def comment_update(request, feedID, commentID):
    data = request.POST
    feed = get_object_or_404(Feed, pk = feedID)
    comment = get_object_or_404(Comment, feed = feed, pk = commentID)
    if data.get('content'):
        comment.content = data.get('content')
    comment.save()
    return Response({"status":"UPDATE"}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def comment_delete(request, feedID, commentID):
    feed = get_object_or_404(Feed, pk = feedID)
    comment = get_object_or_404(Comment, feed = feed, pk = commentID)
    comment.delete()
    return Response({"status":"DELETE NO CONTENT"}, status=status.HTTP_204_NO_CONTENT)
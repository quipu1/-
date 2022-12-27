from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import (
    UserListSerializer,
    UserSerializer,
    UserFriendsSerializer,
    UserAddListSerializer,
)
from django.contrib.auth import (
    get_user_model,
)
from django.db.models import Q
from haversine import haversine


@api_view(['POST'])
def register(request):
    data = request.POST
    User = get_user_model()
    user = User()
    user.userID = data.get('userID')
    user.nickname = data.get('nickname')
    user.password = data.get('password')
    user.save()
    return Response({"status":"Register"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def register_check_userID(rquest, userID):
    User = get_user_model()
    user = User.objects.filter(userID = userID)
    if user:
        return Response({"status":"사용 불가"}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({"status":"사용 가능"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def register_check_nickname(rquest, nickname):
    User = get_user_model()
    user = User.objects.filter(nickname = nickname)
    if user:
        return Response({"status":"사용 불가"}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({"status":"사용 가능"}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def deregister(request, userID):
    user = get_object_or_404(get_user_model(), userID = userID)
    user.delete()
    return Response({"status":"DeRegister"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def user_info(request, userID):
    user = get_object_or_404(get_user_model(), userID = userID)
    serializer = UserSerializer(user)
    return Response(data=serializer.data)


@api_view(['POST'])
def user_info_update(request, userID, column):
    user = get_object_or_404(get_user_model(), userID = userID)
    value = request.POST.get(column)
    if column == 'nickname':
        user.nickname = value
    elif column == 'age':
        user.age = value
    elif column == 'password':
        user.password = value
    elif column == 'profilePhotoPath':
        value = request.FILES['profilePhotoPath']
        user.profilePhotoPath = value
    elif column == 'gender':
        user.gender = value
    elif column == 'latitude':
        user.latitude = value
    elif column == 'logitude':
        user.logitude = value
    print(value)
    user.save()
    return Response({"status":"UPDATE"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(get_user_model(), userID = request.POST.get('userID'))
    if user.password == request.POST.get('password'):
        return Response({"status: login"}, status=status.HTTP_200_OK)
    return Response({"status: login failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_search(request, keyword):
    User = get_user_model()
    users = User.objects.filter(Q(nickname__contains=keyword) | Q(userID__contains=keyword))
    serializer = UserListSerializer(users, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def friends_list(request, userID):
    User = get_user_model()
    user = get_object_or_404(User, userID=userID)
    users = user.friends.all()
    FriendsList = []
    for UserOne in users:
        FriendsList.append(UserOne.userID)
    return Response(data = FriendsList)


@api_view(['GET'])
def request_friend(request, fromA, toB):
    User = get_user_model()
    FromA = get_object_or_404(User, userID=fromA)
    ToB = get_object_or_404(User, userID=toB)
    #이미 친구인경우는 그냥 pass
    if FromA in ToB.friends.all():
        return Response({"status: 이미 친구입니다."}, status=status.HTTP_208_ALREADY_REPORTED)
    #이미 신청한 경우도 pass
    if ToB in FromA.take_list.all():
        return Response({"status: 이미 신청했습니다."}, status=status.HTTP_208_ALREADY_REPORTED)
    #상대가 먼저 신청했을경우(친구 신청 오는걸 받는 경우)
    if FromA in ToB.take_list.all():
        ToB.take_list.remove(FromA)
        ToB.friends.add(FromA)
        ToB.save()
        return Response({"status: 이제 서로 친구입니다."}, status=status.HTTP_201_CREATED)
    FromA.take_list.add(ToB)
    FromA.save()
    return Response({"status: 친구 신청 완료"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def friends_add(request, userID):
    User = get_user_model()
    user = get_object_or_404(User, userID=userID)
    users = user.add_friends.all()
    UserAddList = []
    for UserOne in users:
        UserAddList.append(UserOne.userID)
    return Response(data = UserAddList)


@api_view(['DELETE'])
def friends_remove(request, fromA, toB):
    User = get_user_model()
    FromA = get_object_or_404(User, userID=fromA)
    ToB = get_object_or_404(User, userID=toB)    
    if FromA in ToB.friends.all():
        ToB.friends.remove(FromA)
        return Response({"status: 친구 삭제 완료."}, status=status.HTTP_204_NO_CONTENT)
    if ToB in FromA.take_list.all():
        FromA.take_list.remove(ToB)
        FromA.save()
        return Response({"status: 신청 취소 완료."}, status=status.HTTP_204_NO_CONTENT)
    return Response({"status: 잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def friends_where(request, userID):
    User = get_user_model()
    user = get_object_or_404(User, userID=userID)
    user_where = (user.latitude, user.logitude)
    # print(user_where)
    good_friend = []
    for friend in User.objects.filter(latitude__isnull=False):
            friend_where = (friend.latitude, friend.logitude)
            distance = haversine(user_where, friend_where)*100
            if distance < 1000:
                good_friend.append({"user_id":friend.userID, "nickname" : friend.nickname, "latitude" : friend.latitude,"logitude":  friend.logitude})
                # m 단위로 보내줌, 1000m 이내의 거리
    return Response(data=good_friend)
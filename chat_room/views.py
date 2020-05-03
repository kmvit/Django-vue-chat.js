from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from django.db.models import Q

from django.shortcuts import render
from .models import Room, Chat
from .serializers import RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializers

# Create your views here.

class Rooms(APIView):
    """Комната чата"""
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        rooms = Room.objects.filter(Q(creater=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data':serializer.data})

    def post(self, request):
        Room.objects.create(creater=request.user)
        return Response (status=201)



class Dialog(APIView):
    """Диалог чата"""

    #permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response ({'data':serializer.data})


    def post(self, request):
        room = request.data.get('room')
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            Response(status=400)

class AddUsersRoom(APIView):
    """Добавление юзеров в комнату"""
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        room = request.data.get('room')
        user = request.data.get('user')
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)
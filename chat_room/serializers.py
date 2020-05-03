from rest_framework import serializers
from .models import Room, Chat
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ('id', 'username')

class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнаты чата"""

    creater = UserSerializers()
    invited = UserSerializers(many=True)

    class Meta:
        model = Room
        fields = ('id', 'creater', 'invited', 'date')


class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""

    user = UserSerializers()

    class Meta:
        model = Chat
        fields = ('user', 'text', 'date')


class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация чата POST запрос"""

    class Meta:
        model = Chat
        fields = ('room', 'text' )


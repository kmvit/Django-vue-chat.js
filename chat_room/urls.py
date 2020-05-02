from django.urls import path
from .views import RoomSerializers, Rooms, ChatSerializers, Dialog

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('dialog/', Dialog.as_view()),

]
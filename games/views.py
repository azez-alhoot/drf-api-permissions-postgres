from django.shortcuts import render
from .permissions import IsAuthoeOrReadOnly
from rest_framework import generics

from .models import Game
from .serializer import GameSerializer

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthoeOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer
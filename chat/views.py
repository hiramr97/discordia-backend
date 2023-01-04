from .models import Server
from rest_framework import viewsets
from .serializers import ServerSerializer, ChannelSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ChannelSerializer

from .models import Server
from rest_framework import viewsets
from .serializers import ServerSerializer

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

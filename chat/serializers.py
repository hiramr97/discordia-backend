from rest_framework import serializers
from .models import Server, Channel

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

    channels = ChannelSerializer(
        many=True,
        required = False
    )
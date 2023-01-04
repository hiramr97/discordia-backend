from rest_framework import serializers
from .models import Server, Channel, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'description', 'server', 'messages')
    messages = MessageSerializer(
        many=True,
        required = False
    )

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'name', 'description', 'server_image', 'channels')

    channels = ChannelSerializer(
        many=True,
        required = False
    )
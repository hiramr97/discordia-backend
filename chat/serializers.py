from rest_framework import serializers
from .models import Server, Channel, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'
    messages = MessageSerializer(
        many=True,
        required = False
    )

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

    channels = ChannelSerializer(
        many=True,
        required = False
    )
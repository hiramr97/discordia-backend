from django.db import models

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=21, unique=True)
    description = models.CharField(max_length=100, blank=True)
    server_image = models.ImageField(upload_to='media', blank=True)

class Channel(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='channels')
    name = models.CharField(max_length=21)
    description = models.CharField(max_length=100, blank=True)
    channel_image = models.ImageField(upload_to='media', blank=True)
from rest_framework import routers
from .views import ServerViewSet, ChannelViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register('servers', ServerViewSet, 'servers')
router.register('channels', ChannelViewSet, 'channels')
router.register('messages', MessageViewSet, 'messages')

urlpatterns = router.urls
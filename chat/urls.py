from rest_framework import routers
from .views import ServerViewSet, ChannelViewSet

router = routers.DefaultRouter()
router.register('servers', ServerViewSet, 'servers')
router.register('channels', ChannelViewSet, 'channels')

urlpatterns = router.urls
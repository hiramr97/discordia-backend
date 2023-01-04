from rest_framework import routers
from .views import ServerViewSet, ChannelViewSet

router = routers.DefaultRouter()
router.register('servers', ServerViewSet, 'servers')
router.register('channels', ServerViewSet, 'channels')

urlpatterns = router.urls
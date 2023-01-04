from rest_framework import routers
from .views import ServerViewSet

router = routers.DefaultRouter()
router.register('servers', ServerViewSet, 'servers')
router.register('servers', ServerViewSet, 'servers')

urlpatterns = router.urls
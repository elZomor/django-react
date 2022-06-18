from apps.visitors.views import EventViewSet, ClickViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('home/events', EventViewSet, basename='events')
router.register('click', ClickViewSet, basename='click')

urlpatterns = router.urls



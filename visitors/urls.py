from rest_framework.routers import DefaultRouter
from .views import VisitorViewSet

router = DefaultRouter()
router.register('visitors', VisitorViewSet)

urlpatterns = router.urls
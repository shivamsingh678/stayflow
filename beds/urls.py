from rest_framework.routers import DefaultRouter
from .views import BedViewSet

router = DefaultRouter()
router.register(r'beds', BedViewSet)

urlpatterns = router.urls
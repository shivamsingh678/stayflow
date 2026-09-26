from rest_framework.routers import DefaultRouter
from .views import AllocationViewSet

router = DefaultRouter()
router.register(r'allocations', AllocationViewSet)

urlpatterns = router.urls
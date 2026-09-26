from rest_framework.routers import DefaultRouter
from .views import (
    ComplaintViewSet,
    ComplaintCommentViewSet
)

router = DefaultRouter()

router.register(
    'complaints',
    ComplaintViewSet
)

router.register(
    'comments',
    ComplaintCommentViewSet
)

urlpatterns = router.urls
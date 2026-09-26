from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RentInvoiceViewSet

router = DefaultRouter()
router.register('invoices', RentInvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
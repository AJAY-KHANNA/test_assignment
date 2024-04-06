from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, PlanViewSet, CustomerPlanViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'customer-plans', CustomerPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customers/<int:pk>/', CustomerViewSet.as_view({'patch': 'partial_update'}), name='customer-detail'),
    
]
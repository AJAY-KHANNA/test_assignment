from rest_framework import viewsets
from customer_management.models import Customer, Plan, CustomerPlan
from .serializers import CustomerSerializer, PlanSerializer, CustomerPlanSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class CustomerPlanViewSet(viewsets.ModelViewSet):
    queryset = CustomerPlan.objects.all()
    serializer_class = CustomerPlanSerializer
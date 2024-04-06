from rest_framework.test import APIClient, APITestCase
from customer_management.models import Customer, Plan, CustomerPlan
from django.urls import reverse
from datetime import datetime

class CustomerManagementTestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='John Doe',
            dob='1990-01-01',
            email='johndoe@example.com',
            aadhaar_number='123456789012',
            registration_date='2023-04-06',
            mobile_number='1234567890'
        )
        self.plan = Plan.objects.create(
            name='Platinum365',
            cost=499.00,
            validity=365,
            status='Active'
        )
        self.customer_plan = CustomerPlan.objects.create(
            customer=self.customer,
            plan=self.plan,
            renewal_date='2024-04-06',
            plan_status='Active'
        )

    def test_register_customer(self):
        url = reverse('customer-list')
        data = {
            'name': 'Jane Doe',
            'dob': '1992-05-15',
            'email': 'janedoe@example.com',
            'aadhaar_number': '987654321098',
            'mobile_number': '0987654321',
            'registration_date': '2024-04-06'  # Add registration_date
        }
        client = APIClient()
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 2)


    def test_choose_new_plan(self):
        url = reverse('plan-list')
        data = {
            'name': 'Gold180',
            'cost': 299.00,
            'validity': 180,
            'status': 'Active'
        }
        client = APIClient()
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Plan.objects.count(), 2)

        url = reverse('customerplan-list')
        data = {
            'customer': self.customer.id,
            'plan': Plan.objects.get(name='Gold180').id,
            'renewal_date': '2024-10-06',
            'plan_status': 'Active'
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CustomerPlan.objects.count(), 2)

    def test_update_plan(self):
        url = reverse('customerplan-detail', args=[self.customer_plan.id])
        data = {
            'plan': self.plan.id,  # Reuse existing plan
            'renewal_date': '2024-07-06',
            'plan_status': 'Active'
        }
        client = APIClient()
        response = client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.customer_plan.refresh_from_db()
        expected = '2024-07-06'
        self.assertEqual(self.customer_plan.renewal_date.strftime('%Y-%m-%d'), expected)


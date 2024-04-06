from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    aadhaar_number = models.CharField(max_length=12)
    registration_date = models.DateField()
    mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Plan(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return self.name
    
class CustomerPlan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    renewal_date = models.DateField()
    plan_status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    
    def __str__(self):
        return str(self.customer) + str(" - ") + str(self.plan)
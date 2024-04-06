from rest_framework import serializers
from customer_management.models import Customer, Plan, CustomerPlan

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.email = validated_data.get('email', instance.email)
        instance.aadhaar_number = validated_data.get('aadhaar_number', instance.aadhaar_number)
        instance.registration_date = validated_data.get('registration_date', instance.registration_date)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.save()
        return instance
    
    def validate(self, data):
        errors = {}
        # Validate Aadhaar number
        if 'aadhaar_number' in data:
            aadhaar_number = data['aadhaar_number']
            if len(aadhaar_number) != 12:
                errors['aadhaar_number'] = "Aadhaar number must be 12 digits long."
        # Validate mobile number
        if 'mobile_number' in data:
            mobile_number = data['mobile_number']
            if len(mobile_number) != 10:
                errors['mobile_number'] = "Mobile number must be 10 digits long."
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class CustomerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPlan
        fields = '__all__'
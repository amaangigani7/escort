from rest_framework import serializers
from rest_framework.response import Response
# from phonenumber_field.modelfields import PhoneNumberField
from .models import *
import uuid

class CustomerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerImage
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    # like_details = serializers.CharField()
    get_image_url = CustomerImageSerializer(many=True)

    class Meta:
        model = Customer
        exclude = ('is_staff', 'verification_token', 'forget_password_token', "password", 
                    "is_superuser", "groups", "user_permissions")
        # fields = ('id', 'email', 'user_name', 'full_name', 'dob', 'i_am', 'looking_for',
        #             'created_at')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100, min_length=6)
    user_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    # mobile_number = PhoneNumberField()

    class Meta:
        model = Customer
        fields = ('id', 'user_name', 'email', 'password', "full_name", "i_am", "looking_for",
                    "dob", "city", "created_at")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # print('validated_data= ', validated_data)
        while True:
            auth_token = str(uuid.uuid4())
            if not Customer.objects.filter(verification_token=auth_token).first():
                break
        customer = Customer.objects.create(user_name=validated_data['user_name'], 
                                            email=validated_data['email'],
                                            full_name=validated_data['full_name'],
                                            i_am=validated_data['i_am'],
                                            looking_for=validated_data['looking_for'],
                                            dob=validated_data['dob'],
                                            city=validated_data['city'],
                                            # mobile_number=validated_data['mobile_number'], 
                                            verification_token=auth_token)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer

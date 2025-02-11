from rest_framework import serializers
from .models import Product,Customer
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    """
    serializers.ModelSerializer: A shortcut for creating serializers from models.
    model = Customer: Links the serializer to the Customer model.
    fields = '__all__': Includes all fields from the model in the API.
    """
    class Meta:
        model = Customer
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

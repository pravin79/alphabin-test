from rest_framework import serializers
from .models import Product,Category,Duration,Payment,Address,Cart,Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class DurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duration
        fields = ('id', 'name', 'price')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'card', 'month', 'year', 'user_id')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'addr', 'fullname', 'email', 'country', 'city' 'state', 'pincode', 'user_id')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'qty', 'category_id', 'duration_id', 'product_id', 'user_id')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'qty', 'category_id', 'duration_id', 'product_id', 'user_id')


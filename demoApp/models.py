# Create your models here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Custom email validation logic
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class Product(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False);
    image = models.ImageField()

class Category(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False);

class Duration(models.Model):
    name = models.CharField(max_length=255);
    price = models.IntegerField(blank=False,null=False)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.CharField(max_length=16,blank=False,null=False)
    month = models.IntegerField(blank=False,null=False)
    year = models.IntegerField(blank=False,null=False)

class Cart(models.Model):
    user_id = models.IntegerField(blank=False,null=False)
    product_id = models.IntegerField(blank=False,null=False)
    duration_id = models.IntegerField(blank=False,null=False)
    category_id = models.IntegerField(blank=False,null=False)
    qty = models.IntegerField(blank=False,null=False)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    qty = models.IntegerField(blank=False,null=False)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addr = models.CharField(max_length=500,blank=False,null=False)
    fullname = models.CharField(max_length=255,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    country = models.CharField(max_length=255,blank=False,null=False)
    city = models.CharField(max_length=255,blank=False,null=False)
    state = models.CharField(max_length=255,blank=False,null=False)
    pincode = models.IntegerField(blank=False,null=False)





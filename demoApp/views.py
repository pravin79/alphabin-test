from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserCreationForm
from django.shortcuts import render, redirect

from django.http.response import JsonResponse
import json
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'index.html')
    else:
        return render(request,'homepage.html')

def account(request):
    return render(request,'account.html')

def loginHtml(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def aboutus(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'aboutus.html')
    else:
        return render(request,'aboutus.html')

def checkout(request):
    return render(request,'checkout.html')

def contactus(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'contactus.html')
    else:
        return render(request,'home_contactus.html')



def orderConfirmation(request):
    return render(request,'order-confirmation.html')

def product1(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product1.html')
    else:
        return render(request,'home_product1.html')

def product2(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product1.html')
    else:
        return render(request,'home_product1.html')

def product3(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product1.html')
    else:
        return render(request,'home_product1.html')

def product4(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product1.html')
    else:
        return render(request,'home_product1.html')

def product5(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product1.html')
    else:
        return render(request,'home_product1.html')

def product6(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product1.html')
    else:
        return render(request,'home_product1.html')

def product7(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product1.html')
    else:
        return render(request,'home_product1.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # return render(request, 'homepage.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return JsonResponse("Invalid Login Method",safe=False,status=405)
        # return render(request, 'login.html')
    
def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html')  # Replace 'login' with your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'error': 'User registration failed'})


def logoutHtml(request):
    logout(request)
    return redirect('login')

def myCart(request):
    return render(request,'mycart.html')


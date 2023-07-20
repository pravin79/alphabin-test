from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .models import Cart, Order
import json

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'index.html')
    else:
        return render(request,'homepage.html')

@csrf_exempt
@login_required
def account(request):
    users = User.objects.filter(username = request.user).values()[0]
    return render(request,'account.html',{"user":users})

def loginHtml(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def aboutus(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'aboutus.html')
    else:
        return render(request,'aboutus.html')

@csrf_exempt
@login_required
def checkout(request):
    total=0
    result={}
    result_list=[]
    data = Cart.objects.raw("SELECT 1 as id,demoApp_product.name as product,demoApp_product.image as image,demoApp_duration.name as duration,demoApp_category.name as category,demoApp_duration.price as price ,count(*) as qty FROM  demoApp_cart Join	auth_user on demoApp_cart.user_id=auth_user.id  Join	demoApp_category on demoApp_cart.category_id=demoApp_category.id  Join	demoApp_product on demoApp_cart.product_id=demoApp_product.id  Join	demoApp_duration on demoApp_cart.duration_id=demoApp_duration.id where auth_user.username='"+str(request.user)+"' Group by  demoApp_product.name,demoApp_product.image,demoApp_duration.name,demoApp_category.name,demoApp_duration.price")
    for i in data:
        result['product']=i.product
        result['image']=i.image
        result['duration']=i.duration
        result['category']=i.category
        result['price']=float(i.qty)*float(i.price)
        result['qty']=i.qty
        total = total + float(i.price)*float(i.qty)
        result_list.append(result)
        result={}
    return render(request,'checkout.html',{'result':result_list,'total':total})

@csrf_exempt
def contactus(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'contactus.html')
    else:
        return render(request,'home_contactus.html')

@csrf_exempt
@login_required
def orderConfirmation(request):
    userdata = {}
    userdata['fullname']=request.GET['full-name']
    userdata['email']=request.GET['email']
    userdata['city']=request.GET['city']
    userdata['state']=request.GET['state']
    userdata['country']=request.GET['country']
    userdata['zipcode']=request.GET['zipcode']
    userdata['cardnumber']=request.GET['cardnumber']
    userdata['month']=request.GET['month']
    userdata['year']=request.GET['year']
    userdata['cvv']=request.GET['cvv']
    carts = Cart.objects.all()
    for cart in carts:
        Order.objects.create(
            qty=cart.qty,
            category_id=cart.category_id,
            duration_id=cart.duration_id,
            product_id=cart.product_id,
            user_id=cart.user_id
        )
    user_id=User.objects.filter(username = request.user).values()[0]['id']
    Cart.objects.filter(user_id=user_id).delete()
    return render(request,'order-confirmation.html',{'userdata':userdata})

@csrf_exempt
def product1(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product1.html')
    else:
        return render(request,'home_product1.html')

@csrf_exempt
def product2(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product2.html')
    else:
        return render(request,'home_product2.html')

@csrf_exempt
def product3(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product3.html')
    else:
        return render(request,'home_product3.html')

@csrf_exempt
def product4(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product4.html')
    else:
        return render(request,'home_product4.html')

@csrf_exempt
def product5(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product5.html')
    else:
        return render(request,'home_product5.html')

@csrf_exempt
def product6(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product6.html')
    else:
        return render(request,'home_product6.html')

@csrf_exempt
def product7(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'product7.html')
    else:
        return render(request,'home_product7.html')

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        if (User.objects.filter(email=request.POST['email']).exists()):
            email = request.POST['email']
            username = User.objects.get(email=email)
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'homepage.html',status=200)
                
            else:
                return render(request, 'login.html', {'error':'Invalid password!'}, status=401)
        else:
            return render(request, 'login.html',{'error':'User does not exist!'}, status=404)
    else:
        return render(request, 'login.html',{'error':'Invalid request method!'}, status=405)

@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        if not (User.objects.filter(email=request.POST['email']).exists()):
            rest={
            }
            rest['csrfmiddlewaretoken']=request.POST['csrfmiddlewaretoken']
            rest['first_name']=request.POST['first_name']
            rest['last_name']=request.POST['last_name']
            rest['password1']=request.POST['password1']
            rest['password2']=request.POST['password2']
            rest['email']=request.POST['email']
            rest['username']=str(request.POST['email'])
            form = CustomUserCreationForm(rest)
            if form.is_valid():
                form.save()
                return render(request,'login.html')  # Replace 'login' with your desired redirect URL
            else:
                # Data is invalid, handle the error
                # For example, display error messages to the user
                errors = form.errors
        else:
            return render(request, 'registration.html', {'error': 'Email id already exist!'})        
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'error': errors})

@csrf_exempt
@login_required
def logoutHtml(request):
    logout(request)
    return redirect('login')

@csrf_exempt
@login_required
def myCart(request):
    return render(request,'mycart.html')

@csrf_exempt
def forgotPass(request):
    if (User.objects.filter(email=request.POST['email']).exists()):
        return render(request,'newPassword.html',{'email':str(request.POST['email'])})
    else:
        return render(request,'forgotPassword.html',{'error':'Email id does not exist!'})

@csrf_exempt
def setNewPassword(request):
    email = request.POST['email']
    user = User.objects.get(email=email)
    user.set_password(request.POST['confirmPassword'])
    user.save()
    return render(request,'login.html')
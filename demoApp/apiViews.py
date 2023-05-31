from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from .models import Cart

from .serializers import *

@login_required
def addToCart(request):
    if request.method == 'POST':
        users = User.objects.filter(username = request.user).values()
        user_id = users[0]['id']
        data={
            'user_id':user_id
        }
        data['qty']=0
        data['product_id']=1
        if request.POST.getlist('duration')[0]=='6 Months':
            data['duration_id']=1
        else:
            data['duration_id']=2

        if request.POST.getlist('functionality-testing'):
            data['category_id']=1
            cart = CartSerializer(data=data)
            if cart.is_valid():
                cart.save()
                
            
        if request.POST.getlist('usability-testing'):
            data['category_id']=2
            cart = CartSerializer(data=data)
            if cart.is_valid():
                cart.save()
            
        if request.POST.getlist('performance-testing'):
            data['category_id']=3
            cart = CartSerializer(data=data)
            if cart.is_valid():
                cart.save()
            
        if request.POST.getlist('security-testing'):
            data['category_id']=4
            cart = CartSerializer(data=data)
            if cart.is_valid():
                cart.save()
        if request.POST.getlist('button1')[0]=='2':
            return JsonResponse("Product added to cart successfully.", safe=False,status=200)
        else:
            return redirect('mycart')
            

# @csrf_exempt
# def getEmployee(request,id=0):
#     if request.method=='POST':
#         emp_data = JSONParser().parse(request)
#         temp = Token.objects.filter(token = emp_data['token'])
#         try:
#             if len(temp)!=0:
#                 users = Employee.objects.filter(email = emp_data['email'])
#                 if users:
#                     user_serializer=UserSerializer(users,many=True)
#                     return JsonResponse(user_serializer.data, safe=False,status=200)
#                 else:
#                     return JsonResponse("Invalid Request Data", safe=False,status=422)
#             else:
#                 return JsonResponse("Invalid Token", safe=False,status=422)
#         except requests.exceptions.RequestException as e:
#                     return e
#     else:
#         return JsonResponse("Invalid Request Method", safe=False,status=422)

# def registration(request):
#     if request.method=='POST':
#         temp =  User.objects.filter(email = request.POST['email'])
#         print(len(temp))
#         try:
#             user_serializer = UserSerializer(data=request.POST)
#             if user_serializer.is_valid() and len(temp) == 0:
#                 user_serializer.save()
#                 return render(request,'SuccessPage.html',{"status":"Added Successfully","status":201})
#             else:
#                 return JsonResponse("Registration Failed", safe=False,status=400)
#         except requests.exceptions.RequestException as e:
#             return JsonResponse(e, safe=False,status=400)



@login_required 
def getUser(request):
    if request.method == 'GET':
       return 'Testing'
@login_required
def mycart(request):
    result={}
    result_list=[]
    data = Cart.objects.raw("SELECT demoApp_cart.id as id, demoApp_product.name as product,demoApp_product.image as image,demoApp_duration.name as duration,demoApp_category.name as category,demoApp_duration.price as price FROM  demoApp_cart Join	auth_user on demoApp_cart.user_id=auth_user.id  Join	demoApp_category on demoApp_cart.category_id=demoApp_category.id  Join	demoApp_product on demoApp_cart.product_id=demoApp_product.id  Join	demoApp_duration on demoApp_cart.duration_id=demoApp_duration.id where auth_user.username='"+str(request.user)+"'")
    for i in data:
        result['product']=i.product
        result['image']=i.image
        result['duration']=i.duration
        result['category']=i.category
        result['price']=i.price
        result_list.append(result)
    return render(request,'mycart.html',{'result':result_list})

@login_required
def account(request):
    return render(request,'account.html')



# from django.db import models

# # Create a model
# class Person(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     birth_date = models.DateField()

# class Address(models.Model):
#     street_address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     zip_code = models.CharField(max_length=255)

# # Create a raw query
# query = models.Person.objects.raw('SELECT person.first_name, person.last_name, address.street_address, address.city, address.state, address.zip_code FROM person INNER JOIN address ON person.id = address.person_id')

# # Iterate over the results
# for person in query:
#     print(person.first_name, person.last_name, person.street_address, person.city, person.state, person.zip_code)

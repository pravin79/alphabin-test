from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Cart,Product,Duration,Category,Order

from .serializers import *
@csrf_exempt
@login_required
def deleteProduct(request):
    user_id=User.objects.filter(username=request.user).values()[0]['id']
    product_id=Product.objects.filter(name=request.GET['product']).values()[0]['id']
    duration_id=Duration.objects.filter(name=request.GET['duration']).values()[0]['id']
    category_id=Category.objects.filter(name=request.GET['category']).values()[0]['id']
    rs_delete = Cart.objects.filter(user_id=user_id,product_id=product_id,duration_id=duration_id,category_id=category_id).values()[0]['id']
    deleted = Cart.objects.filter(id=rs_delete).delete()
    return redirect('mycart')

@csrf_exempt
@login_required
def addToCart(request):
    if request.method == 'POST':
        users = User.objects.filter(username = request.user).values()
        user_id = users[0]['id']
        data={
            'user_id':user_id
        }
        data['qty']=1
        data['product_id']=request.POST.getlist('product')[0]
        
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
            if request.POST.getlist('product')[0]=='1':
                return render(request,'home_product1.html',{'message':'Product added to cart successfully!'}, status=201)
            elif request.POST.getlist('product')[0]=='2':
                return render(request,'home_product2.html',{'message':'Product added to cart successfully!'}, status=201)
            elif request.POST.getlist('product')[0]=='3':
                return render(request,'home_product3.html',{'message':'Product added to cart successfully!'}, status=201)
            elif request.POST.getlist('product')[0]=='4':
                return render(request,'home_product4.html',{'message':'Product added to cart successfully!'}, status=201)
            elif request.POST.getlist('product')[0]=='5':
                return render(request,'home_product5.html',{'message':'Product added to cart successfully!'}, status=201)
            elif request.POST.getlist('product')[0]=='6':
                return render(request,'home_product6.html',{'message':'Product added to cart successfully!'}, status=201)
            elif request.POST.getlist('product')[0]=='7':
                return render(request,'home_product7.html',{'message':'Product added to cart successfully!'}, status=201)
            return JsonResponse("Product added to cart successfully.", safe=False,status=200)
        else:
            return redirect('mycart')
@csrf_exempt
@login_required
def order_history(request):
    total=0
    result={}
    result_list=[]
    data = Order.objects.raw(
        ("SELECT "
         "1 as id "
         ",demoApp_product.name as prod "
         ",demoApp_product.image as image "
         ",demoApp_duration.name as durat "
         ",demoApp_category.name as cate "
         ",demoApp_duration.price as price  "
         ",count(*) as qty  "
         "FROM  demoApp_order  "
         "Join	auth_user on demoApp_order.user_id=auth_user.id   "
         "Join	demoApp_category on demoApp_order.category_id=demoApp_category.id   "
         "Join	demoApp_product on demoApp_order.product_id=demoApp_product.id   "
         "Join	demoApp_duration on demoApp_order.duration_id=demoApp_duration.id  "
         "where auth_user.username='"+str(request.user)+"' and demoApp_order.orderNo='"+request.GET['orderno'].strip()+"'"
         "Group by  demoApp_product.name,demoApp_product.image,demoApp_duration.name,demoApp_category.name,demoApp_duration.price"))
    for i in data:
        result['product']=i.prod
        result['image']=i.image
        result['durat']=i.durat
        result['category']=i.cate
        result['price']=float(i.qty)*float(i.price)
        result['qty']=i.qty
        total = total + float(i.price)*float(i.qty)
        result_list.append(result)
        result={}
    return render(request,'orderDetails.html',{'result':result_list,'total':total})


@csrf_exempt
@login_required
def getOrders(request):
    total=0
    result={}
    result_list=[]
    data = Order.objects.raw(
        ("SELECT "
         "1 as id "
         ",count(*) as qty  "
         ",sum(demoApp_duration.price) as price"
         ",demoApp_order.OrderNo as OrderNo"
         " FROM  demoApp_order  "
         " Join	auth_user on demoApp_order.user_id=auth_user.id   "
         "Join	demoApp_duration on demoApp_order.duration_id=demoApp_duration.id  "
         " where auth_user.username='"+str(request.user)+"'  "
         " Group by  demoApp_order.orderNo"
         " Order by OrderNo desc"))
    print(data)
    for i in data:
        result['qty']=i.qty
        result['OrderNo']=i.OrderNo
        result['price']=i.price
        result_list.append(result)
        result={}
    return render(request,'order-history.html',{'result':result_list,'total':total})


@csrf_exempt
@login_required 
def getUser(request):
    if request.method == 'GET':
       return 'Testing'
@csrf_exempt
@login_required
def mycart(request):
    total=0
    result={}
    result_list=[]
    data = Cart.objects.raw("SELECT 1 as id,demoApp_product.name as product,demoApp_product.image as image,demoApp_duration.name as duration,demoApp_category.name as category,demoApp_duration.price as price ,count(*) as qty FROM  demoApp_cart Join	auth_user on demoApp_cart.user_id=auth_user.id  Join	demoApp_category on demoApp_cart.category_id=demoApp_category.id  Join	demoApp_product on demoApp_cart.product_id=demoApp_product.id  Join	demoApp_duration on demoApp_cart.duration_id=demoApp_duration.id where auth_user.email='"+str(request.user)+"' Group by  demoApp_product.name,demoApp_product.image,demoApp_duration.name,demoApp_category.name,demoApp_duration.price")
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
    return render(request,'mycart.html',{'result':result_list,'total':total})
@csrf_exempt
@login_required
def account(request):
    
    return render(request,'account.html')

@csrf_exempt
def forgotPassGuest(request):
    return render(request,'forgotPassword.html')

@csrf_exempt
def updateAccount(request):
    user = User.objects.get(username=request.user)
    user.first_name = request.POST['fname']
    user.last_name = request.POST['lname']    
    user.email = request.POST['email']
    user.save()
    return redirect('account')

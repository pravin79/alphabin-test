from django.urls import path
from . import views, apiViews
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('account',views.account,name='account'),
    path('login',views.loginHtml, name='login'),
    path('registration',views.registration, name='registration'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('checkout',views.checkout,name='checkout'),
    path('contactus',views.contactus,name='contactus'),
    path('mycart',apiViews.mycart,name='mycart'),
    path('orderConfirmation',views.orderConfirmation,name='orderConfirmation'),
    path('product1',views.product1,name='product1'),
    path('product2',views.product2,name='product2'),
    path('product3',views.product3,name='product3'),
    path('product4',views.product4,name='product4'),
    path('product5',views.product5,name='product5'),
    path('product6',views.product6,name='product6'),
    path('product7',views.product7,name='product7'),
    path('loginUser',views.loginUser,name='loginUser'),
    path('registerUser',views.registerUser,name='registerUser'),    
    path('getUser',apiViews.getUser,name='getUser'),    
    path('logout',views.logoutHtml,name='logout'),   
    path('addToCart',apiViews.addToCart,name='addToCart'),  
    path('deleteProduct',apiViews.deleteProduct,name='deleteProduct'),
    path('orderHistory',apiViews.order_history,name='orderHistory'),
    path('forgotPassGuest',apiViews.forgotPassGuest,name='forgotPassGuest'),
    path('forgotPass',views.forgotPass,name='forgotPass'),
    path('setNewPassword',views.setNewPassword,name='setNewPassword'),
    path('updateAccount',apiViews.updateAccount,name='updateAccount'),
    
    

]

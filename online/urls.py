from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns=[

   url(r'^$',views.index,name='index'),
   url(r'^home$',views.home,name='home'),
   url(r'^Login$',views.Login,name='Login'),
   url(r'^Biriyani$',views.Biriyani,name='Biriyani'),
   url(r'^Meals$',views.Meals,name='Meals'),
   url(r'^FastFoods$',views.FastFoods,name='FastFoods'),
   url(r'^Tifins$',views.Tifins,name='Tifins'),
   url(r'^IceCreams$',views.IceCreams,name='IceCreams'),
   url(r'^Sign$',views.Sign,name='Sign'),
   url(r'^MakeOrder$',views.MakeOrder,name='MakeOrder') ,
   url(r'^SignUp_view$',views.SignUp_view,name='SignUp_view'),
   url(r'^Login_view$',views.Login_view,name='Login_view'),
   url(r'^end$',views.end,name='end'),
   url(r'^LogOut',views.LogOut,name='LogOut')
   
  
   



]
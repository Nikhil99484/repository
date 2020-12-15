from django.urls import path
from crmapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product',views.products,name='product'),
    path('customer/<str_pk>',views.customers,name='customer'),
    path('create_order/',views.create_order,name='create_order'),
    path('update_order/<pk>',views.update_order,name='update_order'),
    path('delete_order/<pk>',views.delete_order,name='delete_order'),
    path('update_customer/<pk>',views.update_customer,name='update_customer'),
    path('delete_customer/<pk>',views.delete_customer,name='delete_customer'),
    path('update_product/<pk>',views.update_product,name='update_product'),
    path('delete_product/<pk>',views.delete_product,name='delete_product'),
    path('register/',views.registerview,name='register'),
 #   path('login/',views.login,name='login'),
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('user/',views.userpage,name='user-page')
 ]

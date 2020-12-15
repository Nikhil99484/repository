from django.shortcuts import render,redirect
from .models import Customers,Products,Orders
from .forms import OrderForm,CustomerForm,ProductForm,userform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .decorators import unauthenticated_user,allowed_user,admin_only


@unauthenticated_user
def registerview(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            user=request.POST.get('username')
            messages.success(request,'SUccessfully Acount Is Created For'+user)
        return redirect('login')
    context={'form':form}
    return render(request, 'crm2accounts/register.html', context)

def logoutview(request):
    logout(request)
    return redirect('login')
@unauthenticated_user
def loginview(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'uesrname or password is wrong')
    return render(request,'crm2accounts/login.html')

@login_required(login_url='login')
@allowed_user(allowed_roles=['customers'])
def userpage(request):
    customer=Customers.objects.get(user=request.user)
# customers = Customers.objects.get(user=request.user)
    orders = request.user.customers.orders_set.all()
    total_order = len(orders)
    deliverd = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    outfordelivery = orders.filter(status='Outfordelivery').count()
    context = {'customer': customer, 'orders': orders,
               'total_order': total_order, 'deliverd': deliverd,
               'pending': pending, 'outfordelivery': outfordelivery}
    #context={}
    return render(request,'crm2accounts/user.html',context)

@login_required(login_url='login')
#@allowed_user(allowed_roles=['admin'])
@admin_only
def home(request):
    customers = Customers.objects.all()
    orders = Orders.objects.all()
    total_order = len(orders)
    deliverd = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    outfordelivery = orders.filter(status='Outfordelivery').count()

    context = {'customers': customers, 'orders': orders,
               'total_order': total_order, 'deliverd': deliverd,
               'pending': pending, 'outfordelivery':outfordelivery}
    return render(request,'crm2accounts/dashboard.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])

def customers(request,str_pk):
    customers = Customers.objects.get(id=str_pk)
    orders = customers.orders_set.all()
    total_orders = orders.count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_orders }
    return render(request,'crm2accounts/customers.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request,'crm2accounts/products.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])

def create_order(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'crm2accounts/create_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])

def update_order(request,pk):
    order=Orders.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'fomr':form}
    return render(request, 'crm2accounts/update_orderform.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])

def delete_order(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('/')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])

def update_customer(request,pk):
    customer=Customers.objects.get(id=pk)
    form=CustomerForm(instance=customer)
    if request.method=='POST':
        form=CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'crm2accounts/update_customer.html',context)
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])

def delete_customer(request,pk):
    customer=Customers.objects.get(id=pk)
    customer.delete()
    return redirect('/')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])

def update_product(request,pk):
    product=Products.objects.get(id=pk)
    form=ProductForm(instance=product)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')
    context={'form':form}
    return render(request,'crm2accounts/product_updateform.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])

def delete_product(request,pk):
    product=Products.objects.get(id=pk)
    product.delete()
    return redirect('/')




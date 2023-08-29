from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . forms import UserRegistrationForm, CustomerForm
from django.contrib import messages
from django.views import View

def home(request):
 dels_of_the_day_products = Products.objects.all()
 cosmetics_obj = Categories.objects.get(name='Cosmetics')
 cosmetics = Products.objects.filter(categories=cosmetics_obj.id)
 categories = Categories.objects.all()
 context = {'dels_of_the_day_products':dels_of_the_day_products,'cosmetics':cosmetics,'categories':categories}
 return render(request, 'app/home.html',context)

# def base_file(request):
#  categories = Categories.objects.all()
#  context = {'categories':categories}
#  return render(request, 'app/base.html',context)

def product_detail(request,id):
 single_product = Products.objects.get(id=id)
 categories = Categories.objects.all()
 context={'categories':categories,'single_product':single_product}
 return render(request, 'app/productdetail.html',context)

def categories_page(request,id):
 products = Products.objects.filter(categories=id)
 categories = Categories.objects.all()
 display_categori = Categories.objects.get(id=id)
 context = {'categories':categories,'products':products,'display_categori':display_categori}
 return render(request, 'app/categories_page.html',context)

def filter_price(request, data, id):
 print(data,id)
 cosmetics_obj = Categories.objects.get(name=data)
 if id == 1000:
  filtered_product = Products.objects.filter(categories=cosmetics_obj.id).filter(discounted_price__gt=id)
 else:
    filtered_product = Products.objects.filter(categories=cosmetics_obj.id).filter(discounted_price__lt=1000)
 categories = Categories.objects.all()
 context = {'categories':categories,'products':filtered_product, 'display_categori':data}
 return render(request, 'app/categories_page.html',context)

def customerregistration(request):
 if request.method == 'POST':
  get_form_data = UserRegistrationForm(request.POST)
  if get_form_data.is_valid():
   get_form_data.save()
   messages.success(request,'Your Registration complete successfully!')
 form = UserRegistrationForm()
 context = {'form':form}
 return render(request,'app/customerregistration.html',context)

def login_page(request):
 if request.method == 'POST':
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = authenticate(username=username, password=password)
  if user !=None:
    login(request, user)
    messages.success(request,'You have loggedin Succesfully !!')
    return redirect('profile')
   # user = authenticate(login_form)
 else:
  login_form = AuthenticationForm()
 context = {'form':login_form}
 return render(request, 'app/login.html', context)

class CustomerProfileView(View):
 def get(self,request):
  form = CustomerForm()
  context = {'form':form, 'active':'btn-primary'}
  return render(request,'app/profile.html',context)
 
 def post(self,request):
  user = request.user
  form = CustomerForm(request.POST)
  if form.is_valid():
   name = form.cleaned_data['name']
   address = form.cleaned_data['address']
   city = form.cleaned_data['city']
   distric = form.cleaned_data['distric']
   zip_code = form.cleaned_data['zip_code']
   address_add = Customer(user=user,name=name,address=address,city=city,distric=distric,zip_code=zip_code)
   address_add.save()
   messages.success(request,'Address Added Successfully!!!')
   form = CustomerForm()
   context = {'form':form,'active':'btn-primary'}
   return render(request,'app/profile.html',context)

def address(request):
 addresses = Customer.objects.all()
 context = {'addresses':addresses,'active':'btn-primary'}
 return render(request, 'app/address.html',context)



def add_to_cart(request,id):
 user = request.user
 product_ins = Products.objects.get(id=id)
 add_to_cart = Cart(user=user,product=product_ins)
 add_to_cart.save()
 return redirect('cart')

def show_cart(request):
 user = request.user
 products = Cart.objects.filter(user=user)
 total_ammount = 0.00
 shipping_charge = 70.00
 for product in products:
  temp_ammount = product.product.discounted_price * product.quantity
  total_ammount += temp_ammount
 total_payable = total_ammount+shipping_charge
 context = {'products':products,'total_payable':total_payable,'shipping_charge':shipping_charge,'total_ammount':total_ammount}
 return render(request, 'app/addtocart.html',context)

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')



def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# def mobile(request):
#  return render(request, 'app/mobile.html')



# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

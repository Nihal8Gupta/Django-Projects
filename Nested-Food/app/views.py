from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signin(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        passw = request.POST.get('pass1')

        chech_user = authenticate(username=email,password=passw)
        if chech_user and chech_user.is_active:
            login(request,chech_user)
            request.session['username']=chech_user.first_name
            context.update({'message':'Login successfull !!','class':'alert-success'})
            return HttpResponseRedirect(reverse('index'))
        else:
            context.update({'message':'Invalid Credentials !!','class':'alert-danger'})

    return render(request,'login.html',context)


def index(request):
    d={}
    if request.session.get('username'):
        FN = request.session.get('username')
        user = User.objects.get(first_name=FN)
        d['user'] = user 
    d["All"] = User.objects.all()  
    return render(request,'index.html',d)

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact_us(request):
    d={}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')

        obj = Contact(name=name,email=email,subject=sub,message=msg)
        obj.save()
        d['message']=f'Dear {name} ,Thanks for your time !!'
        
    return render(request,'contact.html',d)

def register(request):
    d={}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('mobile')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password == password2:
            try:
                usr = User.objects.create_user(username=email,email=email,password=password)
                usr.first_name = name
                usr.save()
                
                profile = Profile(user=usr,contact=number)
                profile.save()
                d['status1'] = f"Dear {name}, Register Successfully !!"
            except :
                d['status2'] = f"Dear {name},This email already exists !!"
        else:
            messages.warning(request,'Passwords do not match!!')
            return redirect('/register')


    return render(request,'register.html',d)


def booking(request):
    return render(request,'booking.html')

def feature(request):
    return render(request,'feature.html')

def menu(request):
    if request.method == "POST":
        pass
    else:
        Cat = Category.objects.all()
    return render(request,'menu.html',{'category':Cat})

def single(request):
    return render(request,'single.html')

def team(request):
    return render(request,'team.html')

def dish(request,id):
    c=Category.objects.get(pk=id)
    d=Dish.objects.filter(category=c)
    return render(request,'dish.html',{'dish':d})

@login_required(login_url='login')
def cart(request,id):
    obj = Dish.objects.get(id=id)
    NWO,created = Dish_cart.objects.get_or_create(name=obj)
    
    if created:
        NWO.ammount=obj.price
        NWO.counter = 1
    else:
        NWO.counter += 1
        NWO.ammount=obj.price*NWO.counter
    NWO.save()
    
    cart_list = Dish_cart.objects.all()
    m = 0
    for d in cart_list:
        m = m + (d.name.price * d.counter)

    return render(request,'cart.html',{'cart':cart_list,'M':m})

@login_required(login_url='login')
def cartall(request):
    cart_list = Dish_cart.objects.all()
    m = 0
    for d in cart_list:
        m = m + (d.name.price * d.counter)

    return render(request,'cart.html',{'cart':cart_list,'M':m})

def qntysub(request,id):
    obj = Dish.objects.get(id=id)
    meal = Dish_cart.objects.get(name=obj)
    if meal.counter > 0:
        meal.counter -= 1
        meal.ammount -= obj.price
        meal.save()
    Dish_cart.objects.filter(counter=0).delete()
    
    return redirect('/cart')

def qntyadd(request,id):
    obj = Dish.objects.get(id=id)
    meal = Dish_cart.objects.get(name=obj)
    meal.counter += 1
    meal.ammount += obj.price
    meal.save()
    
    return redirect('/cart')
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
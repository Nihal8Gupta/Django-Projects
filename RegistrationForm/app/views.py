from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
def home(request,d):
    return render(request,'home.html',d)


def register(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        email =request.POST.get('email')
        pass1 =request.POST.get('password1')
        pass2 =request.POST.get('password2')
        
        if pass1 == pass2:
            new_user = User.objects.create_user(username,email,pass1)
            new_user.save()
            messages.success(request,'user has been created successfully!!')
            return redirect('login')
        else:
            messages.warning(request,'Incorrect Password try agian!!')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('pass')
        print(uname,passw)
        user = authenticate(request,username=uname,password=passw)
        if user is not None:
            d = {'name':uname}
            return render(request,'home.html',d)
        else:
            messages.warning(request,'Username or password is incorrect please try again!!')
        
    return render(request,'login.html')
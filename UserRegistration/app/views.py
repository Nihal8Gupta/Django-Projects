from django.http import HttpResponse
from django.shortcuts import render
from app.forms import *
from django.contrib.auth.models import User
from app.models import *

# Create your views here.

def register(requset):
    PEF = ProfileForm()
    UEF = UserForm()
    if requset.method =='POST' and requset.FILES:
        PDF = ProfileForm(requset.POST,requset.FILES)
        UDF = UserForm(requset.POST)
        if PDF.is_valid() and UDF.is_valid():
            #mutable to immutable
            UCO = UDF.save(commit = False)
            pw = UDF.cleaned_data['password']
            UCO.set_password(pw)

            # UCO.save()

            PCO = PDF.save(commit = False)
            PCO.user=UCO
            # PCO.save()
            return HttpResponse('<h1>User has been created!!</h1>')
        else:
            return HttpResponse('<h1>Validation error!!</h1>')
    

    return render(requset,'registerf.html',{'UEF':UEF,'PEF':PEF})
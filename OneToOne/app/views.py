from django.db.models.functions import Length
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def insert_capital(request):
    Capital_name = input('Enter Capital Name=')
    obj = Capital.objects.get_or_create(Capital_name=Capital_name)[0]
    obj.save()
    return HttpResponse('<h1>Row created for Capital!!</h1>')

def insert_country(request):
    CN = input('Enter Country Name=')
    Cn = input('Enter Capital Name=')
    co = Capital.objects.get(Capital_name=Cn)
    obj = Country.objects.get_or_create(Country_Name=CN,Capital_name=co)[0]
    obj.save()
    return HttpResponse('<h1>Row created for Country!!</h1>')

def home(request):
    country=Country.objects.order_by('-Capital_name') #Desc based on character
    capital=Capital.objects.order_by(Length('Capital_name'))
    dept=DEPT.objects.order_by(Length('DEPT_Name').desc())  #Desc based on lenth
    emp=EMP.objects.order_by('EMP_Name')
    d={'Country':country,'Capital':capital,'DEPT':dept,'EMP':emp}
    return render(request,'home.html',d)

def home1(request):

    country=Country.objects.all()
    capital=Capital.objects.all()
    dept=DEPT.objects.all()
    emp=EMP.objects.all()
    d={'Country':country,'Capital':capital,'DEPT':dept,'EMP':emp}
    return render(request,'home.html',d)


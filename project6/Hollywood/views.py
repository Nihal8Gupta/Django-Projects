from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def titanic(request):
    return render(request,'titanic.html')
def harrypotter(request):
    return HttpResponse('<h1>Harry Potter</h1>')
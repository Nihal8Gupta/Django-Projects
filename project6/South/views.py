from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def timestory(request):
    return render(request,'time.html')
def tholiprema(request):
    return HttpResponse('<h1><marquee>TholiPrema</marquee></h1>')
def home(request):
    return render(request,'home.html')
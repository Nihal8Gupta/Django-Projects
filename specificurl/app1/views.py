from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    return render(request,'main.html')
def home(request):
    return HttpResponse('<h1>App1 Home</h1>')
def thome(request):
    return render(request,'home.html')
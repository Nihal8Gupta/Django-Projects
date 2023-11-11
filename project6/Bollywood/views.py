from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def robot(request):
    return render(request,'robot.html')
def creature(request):
    return HttpResponse('<h1>Creature 3D</h1>')
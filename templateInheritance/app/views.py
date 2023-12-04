from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def child(request):
    return render(request,'child.html')
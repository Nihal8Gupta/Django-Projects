from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app2/home.html')
from django.shortcuts import render

# Create your views here.
def page1(request):
    return render(request,'home.htm')
def page2(request):
    return render(request,'cricket.html')
def page3(request):
    return render(request,'page3.html')
def page4(request):
    return render(request,'page4.html')
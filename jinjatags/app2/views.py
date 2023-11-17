from django.shortcuts import render

# Create your views here.
def login(request):
    d={'name1':'Nihal','name2':'Himanshu'}
    return render(request,'login.html',context=d)
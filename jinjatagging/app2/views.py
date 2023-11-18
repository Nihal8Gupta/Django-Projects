from django.shortcuts import render

# Create your views here.
def login(request):
    detail={'infolist':[{'name':'Nihal','age':21,'course':'Python'},{'name':'Himanshu','age':21,'course':'Java'},{'name':'Akash','age':21,'course':'Mern'}]}
    return render(request,'login.html',context=detail)
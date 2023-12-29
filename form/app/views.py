from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def insertC(request):
    if request.method =='POST':
        cname = request.POST['cname']
        cfee = request.POST['cfee']
        obj = Course.objects.create(Cname=cname,Cfee=cfee)
        obj.save()
        return redirect('/displayC')
    return render(request,'insertC.html')
def display_C(request):
    CO = Course.objects.all()
    return render(request,'displayC.html',{'C':CO})
def insertS(request):
    CO = Course.objects.all()
    if request.method =='POST':
        sid = request.POST['sid']
        sname = request.POST['sname']
        sclass = request.POST['sclass']
        c = request.POST['CI']
        co = Course.objects.get(Cname=c)
        obj = Student.objects.create(Sid=sid,Sname=sname,Sclass=sclass,Scourse=co)
        obj.save()
        return redirect('/displayS')
    return render(request,'insertS.html',{'C':CO})
def display_S(request):
    SO = Student.objects.all()
    return render(request,'displayS.html',{'S':SO})
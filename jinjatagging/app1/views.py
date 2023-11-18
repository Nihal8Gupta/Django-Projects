from django.shortcuts import render,HttpResponse

# Create your views here.
def page1(request):
    
    d={'n1':10,'n2':20}
    return render(request,'page1.html',context=d)

def page2(request):
    d={'n1':50,'n2':70,}
    return render(request,'page2.html',d)

def page3(request):
    d={'n1':2000,'n2':1000,'n3':3000}
    return render(request,'page3.html',d)

def page4(request):
    d={'n1':10,'n2':200,'n3':100}
    return render(request,'page4.html',d)
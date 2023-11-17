from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    data='Himanshu'
    d={'name':data}
    return render(request,'home.html',context=d)
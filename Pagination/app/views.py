from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    obj = School.objects.all()
    paginator = Paginator(obj,3)
    pageno = request.GET.get('page')
    page = paginator.get_page(pageno)
    last = page.paginator.num_pages
    totalpage = [ i+1 for i in range(last) ]
    d={'All':page,"last":last,'totalpage':totalpage}
    return render(request,'index.html',d)
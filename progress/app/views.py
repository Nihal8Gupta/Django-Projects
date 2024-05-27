from django.shortcuts import render
from .forms import *
from django.http import JsonResponse
# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def home(request):
    form = UploadForm(request.POST or None , request.FILES or None)
    print(is_ajax(request))
    if is_ajax(request):
        if form.is_valid():
            form.save()
            return JsonResponse({'message':'success man'})
    return render(request,'main.html',{'form':form})

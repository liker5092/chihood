from django.shortcuts import render

from django.http import HttpResponse
from . import models
# Create your views here.


#库存主页面即登陆主页面

def hood(request):
    print(request)

    return HttpResponse("hello hood!!")


def login(request):
    return render(request,'login.html')
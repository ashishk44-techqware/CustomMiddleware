from django.template.response import TemplateResponse
from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    print("i am Home view")
    return HttpResponse("This is Home Page")


def excep(request):
    print("i am exception view")
    a = 10/0  # agar yha exception occur ho ga us k baad hi MyExcetion midelware chale ga otherwise nhi chale ga
    return HttpResponse("This is Exception Page")


def user_info(request):
    print("i am User_info view")
    context = {"name": "rahul"}
    return TemplateResponse(request,'blog/user_info.html',context=context)

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def brandhome(request):
    return render(request,'brandhome.html')

def brandreturn(request):
    query = request.GET.get('brandid')
    message = "Hello {} brand".format(query)
    template = "brandreturn.html"
    context = {
        'message': message,
    }
    return render(request,template, context)   

def say_hello(request):
    
    return render(request,'hello.html',{'name':'Alberto'})
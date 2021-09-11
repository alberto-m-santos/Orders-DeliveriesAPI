from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def orderhome(request):
    return render(request,'orderhome.html')

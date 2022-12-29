from django.shortcuts import render
from django. http import HttpResponse
# Create your views here.
def teja(request):
    return HttpResponse('<i><b>teja is lazy fellow</b></i>')
def sweety(request):
    return HttpResponse('<marquee><h1>sweety is good girl</h1></marquee>')

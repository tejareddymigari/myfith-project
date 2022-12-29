from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def teja(request):
    return HttpResponse('<marquee><h1>teja reddy</h1></marquee>')
def sweety(request):
    return HttpResponse('<marquee><h2>sweety is most qtest girl</h2></marquee>')
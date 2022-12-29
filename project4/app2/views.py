from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.
def saritha (request):
    return HttpResponse('<i><b>saritha is good</b></i>')
def chintu(request):
    return HttpResponse('<h1><b>chintu is good boy</b></h1>')

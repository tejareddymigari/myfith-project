from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def manu(request):
    return HttpResponse("<h1><marquee>manu is good girl and good person</marquee></h1>")
def mouni(request):
    return HttpResponse('<h1>mouni is tallest girl in jspiders<h1>')
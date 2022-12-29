from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ravi(request):
    return HttpResponse('<marquee> <h1>she is a good girl</h1> </maruqee>')
def ramana(request):
    return HttpResponse ('<h1>he is an inteligent</h1>')

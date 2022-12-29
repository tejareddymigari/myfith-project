from django.urls import path
from app2.views import*
appname='something'
urlpatterns = [
    path('ravi/',ravi,name='ravi'),
    path('ramana/',ramana,name='ramana'),
    
]

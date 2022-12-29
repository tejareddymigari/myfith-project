from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns = [
    path('manu/',manu,name='manu'),
    path('mouni/',mouni,name='mouni'),
    
]

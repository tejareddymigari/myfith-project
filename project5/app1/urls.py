from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns = [
    path('teja/',teja,name='teja'),
    path('sweety/',sweety,name='sweety',)
]


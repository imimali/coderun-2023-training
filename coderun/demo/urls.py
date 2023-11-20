from django.urls import path
from django.http import HttpResponse
from .views import say_hello
app_name = 'demo'

urlpatterns = [

    path('hello', say_hello, name='index'),
]
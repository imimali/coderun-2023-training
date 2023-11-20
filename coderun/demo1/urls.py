from django.urls import path
from django.http import HttpResponse
app_name = 'demo1'
from .views import say_hello
urlpatterns = [
    path('', say_hello, name='index'),
]
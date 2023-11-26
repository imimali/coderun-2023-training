# Django Dash - An introduction to Web Development for Speedsters

![](pics/DALL·E%202023-11-20%2016.28.34%20-%20An%20imaginative%20illustration%20representing%20Django%20as%20a%20web%20framework%20and%20the%20concept%20of%20speed.%20The%20image%20should%20feature%20a%20sleek,%20futuristic%20racetrack%20wi.png)

## Introduction

Welcome to Django Dash! This is a workshop designed to introduce you to the world of web development using Django, a Python web framework. 
We will be building a simple web application.

## Installation, creating a new project
I assume you already have Python installed. If you don't, you can download it from [here](https://www.python.org/downloads/).
## Creating a virtual environment (optional, but recommended)
```bash
pip install virtualenv
```
Now create a virtual environment
```bash
python -m venv venv
```

Now activate the virtual environment
```bash
source venv/bin/activate
```
Or on windows
```bash
venv\Scripts\activate
```

This will isolate your installation so you don't have to worry about messing up your system installation.

## Now let's Django

```bash
pip install Django
```
Easy enough, right? Now let's create a new project.
```bash
django-admin startproject coderun
```
:bulb: `startproject` vs `startapp`

```bash
>> cd coderun
>> django-admin startproject demo
```
Explore the files and folders created by the command. You should see something like this:
```
coderun
├── coderun
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
Let's test if it worked:
```bash
>> python manage.py runserver
```
Let's create an app now:

```bash
>> python manage.py startapp demo
```
Now you should see something like this:
```
coderun
├── coderun
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── demo
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
```
## Creating a simple view
Let's create a simple view. Open `demo/views.py` and add the following code:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
```
Now we need to tell Django to use this view. Open `demo/urls.py` and add the following code:
```python
from .views import index
from django.urls import path
 urlpatterns = [
    path('', index, name='index'),
]
```

## Creating a simple template
Let's create a simple template. Create a new folder called `templates` in the `demo` folder. Create a new file called `index.html` in the `templates` folder and add the following code:
```html
<div>
        {% if books %}

        {% for book in books%}
        <h1>Title: {{ book.title }}</h1>
        <h1>Author: {{ book.author }}</h1>
        {% endfor %}
        {% endif %}
    </div>
```
Now we need to tell Django to use this template. Open `demo/views.py` and add the following code:
```python
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        


def index(request):
    books = [
        Book('The Brothers Karamazov', 'Fyodor Dostoevsky'),
        Book('The Master and Margarita', 'Mikhail Bulgakov'),
    ]
    return render(request, 'index.html', {'books': books})
```
## But hold on, we don't quite usually do it like this 
Let's create a model. Open `demo/models.py` and add the following code:
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```
Now we need to tell Django to use this model. Open `demo/admin.py` and add the following code:
```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```
We didn't do this at the training but now you can do the following:
```bash
>> python manage.py makemigrations
>> python manage.py migrate
```
Now you can add books from the admin panel.
You can go to localhost:8000/admin and login with the credentials you created when you ran `python manage.py createsuperuser`.
If you didn't yet, do it and follow the instructions. It will help you create credentials to log in.

## Creating a simple form
Let's create a simple form. Open `demo/forms.py` and add the following code:
```python
from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
```
You can do this from actual html code, it's just a matter of preference. I personally find it easier to do it like this.
You can take a look at the templates file in the code we wrote and see what kind of magic templating languages are
capable of. Once you get the hang of the syntax, you can do some pretty cool stuff with it.
Here's an explanation of what we've done there
```html
<div>
    <div>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Push me</button>
        </form>
    </div>
    <div>
        {% if books %}

        {% for book in books%}
        <h1>Title: {{ book.title }}</h1>
        <h1>Author: {{ book.author }}</h1>
        {% endfor %}
        {% endif %}
    </div>
</div>
```
- The `{% csrf_token %}`  part was necessary to avoid cross-site request forgery attacks. You can read more about it [here](https://docs.djangoproject.com/en/3.2/ref/csrf/).
- The `{{ form.as_p }}` part took our form passed in the template context and rendered it as a paragraph. You can read more about it [here](https://docs.djangoproject.com/en/3.2/topics/forms/#rendering-fields-manually).
- The `{% if books %}` part is a conditional statement. You can read more about it [here](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#if).
- Analogously, you can do for loops and access the elements of the list. You can read more about it [here](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for). The actual html code will be rendered for each element of the list. You do need th e`{% endfor %}` part to close the loop, analogously for the if as well.












from django.shortcuts import render
from django.http import HttpResponse
import django.forms as forms
from .models import Book

class AddBookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)


# Create your views here.



def say_hello(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            book = Book(author=author,title=title)
            book.save()

    books = Book.objects.all()
    return render(request, 'demo/index.html', context=dict(books=books,form=AddBookForm()))

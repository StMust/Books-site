
from multiprocessing import context
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout, get_user_model
# Create your views here.

User = get_user_model()

def index(request):
    model = Books.objects.all()
    context = {
        'model' : model,
        'cat_selected' : 0
    }
    return render(request, 'main/index.html', context)

def register(request):
    form = RegisterForm(request.POST or None)
    context = {
		'form' : form
	}



    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        new_user = User.objects.create_user(username, email, password)

        return redirect('login')

    return render(request, 'main/auth/register.html', context)


def loginview(request):
    form = LoginForm(request.POST or None)
    context = {'form' : form}

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
            
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            print("Error")
    return render(request, 'main/auth/login.html', context)


def logout_me(request):
    logout(request)
    return redirect('login')

def show_book(request, book_slug):
    book = get_object_or_404(Books, slug = book_slug)
    context = {
        'book' : book
    }

    return render(request, 'main/books.html',context)


def show_category(request, cat_id):
    model = Books.objects.filter(cat_id = cat_id)
    if len(model) == 0:
        raise Http404()
    context ={
        'model' : model,
        'cat_selected' : cat_id,
    }
    return render(request, 'main/index.html', context)

def addbook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid:
            form.save
            return redirect('index')
    else:
        form = AddBookForm()
    context = {
        'form' : form
    }
    return render(request, 'main/add_book.html', context)
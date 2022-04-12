from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name = 'index'),
    path('python_books/', python_books, name = 'python_books'),
    path('c_books/', c_books, name = 'c_books'),
    path('register/',register, name = 'register'),
    path('login/', loginview, name='login'),
    path('logout/', logout_me, name='logout_me'),
    path('book/<slug:book_slug>/', show_book, name = 'show'),
    path('category/<int:cat_id>', show_category , name = 'category')
]
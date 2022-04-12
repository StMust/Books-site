from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name = 'index'),
    path('register/',register, name = 'register'),
    path('login/', loginview, name='login'),
    path('logout/', logout_me, name='logout_me'),
    path('book/<slug:book_slug>/', show_book, name = 'show'),
    path('category/<int:cat_id>/', show_category , name = 'category')
]
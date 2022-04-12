from atexit import register
from django import template

from main.models import *

register = template.Library()

@register.simple_tag(name='menu')
def menu():
    return [
        {'title':'Home', 'url_name' : 'index'},
        {'title':'Python Books', 'url_name' : 'python_books'},
        {'title':'C books', 'url_name' : 'c_books'},
    ]

@register.inclusion_tag('main/list_category.html', name = 'listcats')
def show_categories(sort=None,cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats" : cats, "cat_selected" : cat_selected}
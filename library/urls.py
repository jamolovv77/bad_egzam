from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', add_autor, name='add_autor'),
    path('add_books/',add_books,name='add_books'),
    path('get_books/',get_books, name='get_books'),
    path('add_orders/',add_orders,name='add_orders'),
    path('get_orders/',get_orders, name='get_orders')

]

from .views import *
from django.urls import path

urlpatterns = [
    path('', books, name = 'books'),
    path('create_book/', create_book, name = 'create_book'),
    path('update_book/<int:id>', update_book, name = 'update_book'),
    path('detail_book/<int:id>', detail_book, name = 'detail_book'),
    path('delete_book/<int:id>', delete_book, name = 'delete_book'),
]

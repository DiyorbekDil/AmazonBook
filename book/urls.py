from django.urls import path
from book.views import books_list_view, books_detail_view, create_book_view


app_name = 'book'

urlpatterns = [
    path('<int:pk>', books_detail_view, name='books_detail'),
    path('form/', create_book_view, name='create_book'),
    path('', books_list_view, name='books_list'),
]
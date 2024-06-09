from django.urls import path
from .views import book, books, member, members, add_book, result

urlpatterns = [
    path('book/', books, name='all-books'),
    path('book/<int:book_id>/', book, name='book-detail'),
    path('member/', members, name='all-members'),
    path('member/<int:member_id>/', member, name='members-detail'),
    path('add-book/', add_book, name='add-book'),
    path('result/', result, name='result')
]

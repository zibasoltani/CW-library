from django.test import TestCase
from .models import Book


# Create your tests here.
class BookTest(TestCase):
    def setUp(self):
        Book.objects.create(title='Test Title', author='Test Author', published_date='2022-09-09', ISBN='123',
                            available=1)

    def test_book_init(self):
        book = Book.objects.get(title='Test Title')
        self.assertEqual(book.author, 'Test Author')

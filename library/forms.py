from django import forms
from .models import Book


class BookForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    published_date = forms.DateField()
    ISBN = forms.IntegerField()
    available = forms.BooleanField()

    class Meta:
        model = Book


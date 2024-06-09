from .models import Book, Member, Loan
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import BookForm


def book(request, book_id=None):
    # book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}
    return render(request, 'book.html', context)


def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)


def member(request, member_id=None):
    member = get_object_or_404(Member, id=member_id)
    context = {'member': member}
    return render(request, 'member.html', context)


def members(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'members.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Book.objects.create(**data)
            return HttpResponseRedirect('/result/')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def result(request):
    return render(request, 'result.html')



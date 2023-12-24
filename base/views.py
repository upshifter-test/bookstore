from django.http import HttpResponse
from django.shortcuts import render, redirect

from base.models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'base/index.html', {'books': books})


def book_detail(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if not book:
        return HttpResponse('Book not found')
    return render(request, 'base/detail.html', {'book': book})


def create_book(request):
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        is_available = request.POST.get('is_available')
        cover = request.FILES.get('cover')
        Book.objects.create(
            title=title,
            description=description,
            price=price,
            publish_date=publish_date,
            is_available=is_available,
            cover=cover
        )
        return redirect('index')
    return render(request, 'base/create.html')


def delete_book(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if not book:
        return HttpResponse('Book not found')
    book.delete()
    return redirect('index')


def update_book(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if not book:
        return HttpResponse('Book not found')
    if request.POST:
        book.title = request.POST.get('title', book.title)
        book.description = request.POST.get('description', book.description)
        book.price = request.POST.get('price', book.price)
        book.publish_date = request.POST.get('publish_date', book.publish_date)
        book.is_available = request.POST.get('is_available', book.is_available)
        cover = request.FILES.get('cover')
        if cover:
            book.cover = cover
        book.save()
        return redirect('index')
    return render(request, 'base/update.html', {'book': book})

from django.shortcuts import get_object_or_404, render_to_response
from .models import Book

def book_list(request):
    book_list = get_object_or_404(Book)

    return render_to_response('book/index.html', {'book_list': book_list})

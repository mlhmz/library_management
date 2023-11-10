from django.views.generic import ListView, DetailView

from .models import Book


# Create your views here.
class BookListView(ListView):
    paginate_by = 10
    model = Book
    template_name = 'book_list.html'
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = "book"

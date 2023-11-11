from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import BorrowEntryForm
from .models import Book, BorrowEntry


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


class BookBorrowView(CreateView):
    model = BorrowEntry
    form_class = BorrowEntryForm
    template_name = 'book_borrow.html'
    success_url = reverse_lazy('book_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['book_pk'] = self.kwargs['book_pk']
        return kwargs

    def form_valid(self, form):
        book_pk = self.kwargs['book_pk']
        book = get_object_or_404(Book, pk=book_pk)
        self.object = form.save(commit=False)
        self.object.customer = self.request.user
        self.object.book = book
        self.object.save()
        return super().form_valid(form)

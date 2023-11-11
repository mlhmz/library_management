from django.contrib import messages
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

    def get_queryset(self):
        # print(self.request.content_params['deine_mama'])
        all_books = Book.objects.all()

        # filter id
        query_id = self.request.GET.get('id')
        if query_id is not None:
            all_books = all_books.filter(id=query_id)

        author = self.request.GET.get('author')
        if author is not None:
            all_books = all_books.filter(author__name__icontains=author)

        title = self.request.GET.get('title')
        if title is not None:
            all_books = all_books.filter(title__icontains=title)

        isbn = self.request.GET.get('isbn')
        if isbn is not None:
            all_books = all_books.filter(isbn__icontains=isbn)

        genre = self.request.GET.get('genre')
        if genre is not None:
            genres = genre.split(',')
            for genre in genres:
                all_books = all_books.filter(genres__name__icontains=genre)

        year = self.request.GET.get('year')
        if year is not None:
            all_books = all_books.filter(year__icontains=year)

        all_books = all_books.order_by('-year')
        return all_books


class BorrowedBooksListView(ListView):
    paginate_by = 10
    model = BorrowEntry
    template_name = 'borrowed_books.html'
    context_object_name = "borrowed_books"

    def get_queryset(self):
        return BorrowEntry.objects.all().filter(customer=self.request.user).order_by('-borrowed_from').order_by(
            '-borrowed_from')


class BookBorrowView(CreateView):
    model = BorrowEntry
    form_class = BorrowEntryForm
    template_name = 'book_borrow.html'
    success_url = reverse_lazy('book_list')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['book_pk'] = self.kwargs['book_pk']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        context['borrow_entries'] = BorrowEntry.objects.all().filter(book__pk=self.kwargs['book_pk']).order_by(
            '-borrowed_from')
        return context

    def form_valid(self, form):
        book_pk = self.kwargs['book_pk']
        book = get_object_or_404(Book, pk=book_pk)
        self.object = form.save(commit=False)
        self.object.customer = self.request.user
        self.object.book = book
        self.object.save()
        messages.success(self.request, 'Borrow Timespan booked successfully')
        return super().form_valid(form)

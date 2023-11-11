from django.urls import path

from library import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("borrowed_books", views.BorrowedBooksListView.as_view(), name="borrowed_books"),
    path("borrow/<int:book_pk>", views.BookBorrowView.as_view(), name="book_borrow"),
]

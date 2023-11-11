from django.urls import path

from library import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("borrowed_books", views.BorrowedBooksListView.as_view(), name="borrowed_books"),
    path("borrow/<int:book_pk>", views.BookBorrowView.as_view(), name="book_borrow"),
    path("delete_borrowed_entry/<int:pk>", views.DeleteBorrowedEntryView.as_view(), name="delete_borrowed_entry"),
]

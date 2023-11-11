from django.urls import path

from library import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("borrow/<int:book_pk>", views.BookBorrowView.as_view(), name="book_borrow"),
]

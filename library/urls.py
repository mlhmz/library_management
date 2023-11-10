from django.urls import path

from library import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("<int:pk>", views.BookDetailView.as_view(), name="book_detail"),
    path("borrow/<int:book_pk>", views.BookBorrowView.as_view(), name="book_borrow"),
]

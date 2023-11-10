from django.contrib import admin

from .models import Book, Genre, Author


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    model = Book


class GenreAdmin(admin.ModelAdmin):
    model = Genre


class AuthorAdmin(admin.ModelAdmin):
    model = Author


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)

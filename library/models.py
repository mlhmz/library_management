from django.contrib.auth.models import User
from django.db import models

from library.validators import validate_isbn


class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn = models.CharField(max_length=13, validators=[validate_isbn])
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.title} ({self.year})'


class BorrowEntry(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_from = models.DateField()
    borrowed_to = models.DateField()

    def __str__(self):
        return f'{self.borrowed_from} - {self.borrowed_to}'

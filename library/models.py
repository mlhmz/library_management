from django.db import models


class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre)


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

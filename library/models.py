from django.db import models


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
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.title} ({self.year})'

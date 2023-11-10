import random

from django.utils import timezone
import os

import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library_management.settings")
django.setup()

fake = Faker()

from library.models import Author, Book, Genre

authors = []
for _ in range(10):
    authors.append(Author.objects.create(name=fake.name()))

genres = []
for _ in range(10):
    genres.append(Genre.objects.create(name=fake.word()))


def create_isbn(isbn13):
    if isbn13:
        return fake.isbn13()
    else:
        return fake.isbn10()


def create_book(isbn13):
    book = Book.objects.create(
        title=fake.sentence(),
        author=authors[random.randrange(9)],
        year=fake.year(),
        isbn=fake.isbn13(),
    )
    book.genres.add(genres[random.randrange(9)])
    book.genres.add(genres[random.randrange(9)])
    book.save()



def create_isbn13books(amount):
    for _ in range(amount):
        create_book(True)


def create_isbn10books(amount):
    for _ in range(amount):
        create_book(False)


create_isbn13books(100)
create_isbn10books(100)

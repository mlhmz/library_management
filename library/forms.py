from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput
from django.utils.datetime_safe import datetime

from .models import BorrowEntry


def is_book_available_in_timespan(book_pk, borrowed_from, borrowed_to):
    all_entries = BorrowEntry.objects.all().filter(book__pk=book_pk)
    for entry in all_entries:
        if borrowed_from <= entry.borrowed_to and entry.borrowed_from <= borrowed_to:
            return True
    return False


def is_from_date_after_to_date(from_date, to_date):
    return from_date > to_date


def is_book_in_timespan(borrowed_from, borrowed_to, timespan):
    delta = borrowed_to - borrowed_from
    return delta.days > timespan


def is_borrow_in_past(borrowed_from):
    return borrowed_from < datetime.now().date()


class BorrowEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.book_pk = kwargs.pop('book_pk')
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()

        borrowed_from = cleaned_data.get("borrowed_from")
        borrowed_to = cleaned_data.get("borrowed_to")

        if is_from_date_after_to_date(borrowed_from, borrowed_to):
            raise ValidationError("The From date can't be after the To date.")

        if is_book_in_timespan(borrowed_from, borrowed_to, 14):
            raise ValidationError("The book can't be borrowed for more than 14 days.")

        if is_book_available_in_timespan(self.book_pk, borrowed_from, borrowed_to):
            raise ValidationError("The book is not available in the given timespan.")

        if is_borrow_in_past(borrowed_from):
            raise ValidationError("The borrow date can't be in the past.")

    class Meta:
        model = BorrowEntry
        fields = ["borrowed_from", "borrowed_to"]
        widgets = {
            'borrowed_from': DateInput(attrs={
                'class': 'input input-bordered',
                'placeholder': 'From',
                'type': 'date'
            }),
            'borrowed_to': DateInput(attrs={
                'class': 'input input-bordered',
                'placeholder': 'To',
                'type': 'date'
            }),
        }

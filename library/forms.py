from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from .models import BorrowEntry, Book


class BorrowEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.book_pk = kwargs.pop('book_pk')
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()

        borrowed_from = cleaned_data.get("borrowed_from")
        borrowed_to = cleaned_data.get("borrowed_to")

        all_entries = BorrowEntry.objects.all().filter(book__pk=self.book_pk)
        for entry in all_entries:
            if borrowed_from <= entry.borrowed_to and entry.borrowed_from <= borrowed_to:
                raise ValidationError("In this timespan, someone else borrowed the book.")

        if borrowed_from > borrowed_to:
            raise ValidationError("The From Date shouldn't be after the To Date")

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

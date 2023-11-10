from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelMultipleChoiceField, ModelChoiceField

from .models import BorrowEntry, Book


class BorrowEntryForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()

        borrowed_from = cleaned_data.get("borrowedFrom")
        borrowed_to = cleaned_data.get("borrowedTo")

        if borrowed_from > borrowed_to:
            raise ValidationError("The From Date shouldn't be after the To Date")

    class Meta:
        model = BorrowEntry
        fields = ["borrowedFrom", "borrowedTo"]
        widgets = {
            'borrowedFrom': DateInput(attrs={
                'class': 'input input-bordered',
                'placeholder': 'From',
                'type': 'date'
            }),
            'borrowedTo': DateInput(attrs={
                'class': 'input input-bordered',
                'placeholder': 'To',
                'type': 'date'
            }),
        }

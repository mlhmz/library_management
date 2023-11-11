from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from .models import BorrowEntry


class BorrowEntryForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()

        borrowed_from = cleaned_data.get("borrowed_from")
        borrowed_to = cleaned_data.get("borrowed_to")

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

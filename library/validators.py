from django.core.exceptions import ValidationError


def validate_isbn(value):
    if len(value) != 10 and len(value) != 13:
        raise ValidationError('ISBN must be 10 or 13 characters long')
    if not value.isdigit():
        raise ValidationError('ISBN must contain only digits')

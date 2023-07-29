from django.core.exceptions import ValidationError


def check_for_capital_first_letter(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def check_string_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')

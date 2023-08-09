from django.core.exceptions import ValidationError


def check_for_capital_first_letter(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def check_string_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')


def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise ValidationError('The maximum file size that can be uploaded is 5MB.')



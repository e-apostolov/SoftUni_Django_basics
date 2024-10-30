from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class AlphaNumericValidator:
    def __init__(self, message=None):
        if message is None:
            message = 'Ensure this value contains only letters, numbers, and underscore.'
        else:
            self.message = message

    def __call__(self, value, *args, **kwargs):
        if value.lower() != slugify(value):
            raise ValidationError(self.message)
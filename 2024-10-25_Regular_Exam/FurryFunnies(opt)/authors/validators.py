from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AuthorNameValidator:
    def __init__(self, message=None):
        if message is None:
            self.message = 'Your name must contain letters only!'
        else:
            self.message = message

    def __call__(self, value, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class AuthorPasscodeValidator:
    def __init__(self, message=None):
        if message is None:
            self.message = 'Your passcode must be exactly 6 digits!'
        else:
            self.message = message

    def __call__(self, value, *args, **kwargs):
        if len(value) != 6 or not value.isdigit():
            raise ValidationError(self.message)

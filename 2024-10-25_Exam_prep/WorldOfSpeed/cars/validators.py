from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CarYearValidator:
    def __init__(self, message=None):
        if message is None:
            self.message = 'Year must be between 1999 and 2030!'
        else:
            self.message = message

    def __call__(self, value, *args, **kwargs):
        if value < 1999 or value > 2030:
            raise ValidationError(self.message)

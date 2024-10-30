from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re

@deconstructible
class UsernameValidator:
    def __init__(self, message=None):
        if message is None:
            message = 'Username must contain only letters, digits, and underscores!'
        else:
            self.message = message

    def __call__(self, value, *args, **kwargs):
        if not re.match(r'^[\w]+$', value):
            raise ValidationError(self.message)
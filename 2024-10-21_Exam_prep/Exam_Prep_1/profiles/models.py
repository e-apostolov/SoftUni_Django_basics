from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.forms import CharField

from profiles.validators import AlphaNumericValidator


# def alpha_numeric_validator(value):
#     if not value.isalnum():
#         raise ValidationError('Only alphanumeric characters are allowed.')

# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator(),
        ]
    )
    email = models.EmailField()
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0.0)],
        blank=True,
        null=True
    )
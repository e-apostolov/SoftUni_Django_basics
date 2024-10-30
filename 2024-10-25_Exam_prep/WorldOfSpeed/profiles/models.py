from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import UsernameValidator


# Create your models here.
class Profile(models.Model):
    MIN_PROFILE_USERNAME_LENGTH = 3
    MIN_PROFILE_AGE = 21
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(
            MIN_PROFILE_USERNAME_LENGTH,
            message=f'Username must be at least {MIN_PROFILE_USERNAME_LENGTH} chars long!'),
                    UsernameValidator()],
    )

    email = models.EmailField()
    age = models.IntegerField(
        validators=[MinValueValidator(
            MIN_PROFILE_AGE,
            message=f'Age requirement: {MIN_PROFILE_AGE} years and above.')]
    )
    password = models.CharField(
        max_length=25,
    )

    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
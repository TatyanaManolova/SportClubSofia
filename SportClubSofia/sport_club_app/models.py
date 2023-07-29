from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from SportClubSofia.sport_club_app.validators import check_for_capital_first_letter, check_string_only_letters


class ClubUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            check_for_capital_first_letter,
            check_string_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            check_for_capital_first_letter,
            check_string_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    # profile_picture = models.URLField(
    #     null=True,
    #     blank=True,
    # )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)

        return result


class Skater(models.Model):
    TYPE_MAX_LENGTH = 35
    SKATER_NAME_MAX_LENGTH = 20
    SKATER_NAME_MIN_LENGTH = 2

    CHOICES = (
        ('CHICKS', 'Chicks'),
        ('CUBS', 'Cubs'),
        ('BASIC NOVICES', 'Basic Novices'),
        ('INTERMEDIATE NOVICES', 'Intermediate Novices'),
        ('ADVANCED NOVICES', 'Adverted Novices'),
        ('JUNIOR', 'Junior'),
        ('SENIOR', 'Senior'),
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=SKATER_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(SKATER_NAME_MIN_LENGTH),
            check_string_only_letters
        )
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=TYPE_MAX_LENGTH,
        choices=CHOICES
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    age = models.IntegerField(
        null=False,
        blank=False
    )

    coach = models.ForeignKey(to=ClubUser, auto_created=True, on_delete=models.DO_NOTHING)


from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from SportClubSofia.sport_club_app.validators import check_for_capital_first_letter, check_string_only_letters, \
    validate_file_size


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

    profile_picture = models.ImageField(validators=(validate_file_size,), blank=True, null=True, upload_to="media/photos")

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

    photo = models.ImageField(validators=(validate_file_size,), upload_to="media/photos")

    category = models.CharField(
        null=False,
        blank=False,
        max_length=TYPE_MAX_LENGTH,
        choices=CHOICES
    )

    age = models.IntegerField(
        null=False,
        blank=False
    )

    coach = models.ForeignKey(to=ClubUser, auto_created=True, on_delete=models.SET_NULL, null=True)


class Competition(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()


# class TrainingSession(models.Model):
#     skater = models.ForeignKey(Skater, on_delete=models.CASCADE)
#     coach = models.ForeignKey(ClubUser, on_delete=models.CASCADE)
#     date = models.DateField()
#     duration = models.IntegerField()
#
#
# class Achievement(models.Model):
#     skater = models.ForeignKey(Skater, on_delete=models.CASCADE)
#     competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
#     rank = models.IntegerField()


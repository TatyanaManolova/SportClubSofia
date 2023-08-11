from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from SportClubSofia.sport_club_app.models import Skater, Competition

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class'
            })
    )


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'class'
            })
        }

    def save(self, commit=True):
        result = super().save(commit)
        return result


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name',  'email', 'profile_picture')
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Profile Picture',
        }


class SkaterBaseForm(forms.ModelForm):
    class Meta:
        model = Skater
        # fields = '__all__'
        exclude = ('coach',)


class SkaterCreateForm(SkaterBaseForm):
    pass


class SkaterEditForm(SkaterBaseForm):
    pass


class SkaterDeleteForm(SkaterBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'


# class TrainingSessionForm(forms.ModelForm):
#     class Meta:
#         model = TrainingSession
#         fields = ['skater', 'coach', 'date', 'duration']
#

class CompetitionBaseForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        # exclude = ('coach',)


class CompetitionCreateForm(CompetitionBaseForm):
    pass


# class CompetitionEditForm(CompetitionBaseForm):
#     pass


# class CompetitionDeleteForm(CompetitionBaseForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__set_readonly_fields()
#
#     def save(self, commit=True):
#         if self.instance:
#             self.instance.delete()
#
#         return self.instance
#
#     def __set_readonly_fields(self):
#         for field in self.fields.values():
#             field.widget.attrs['readonly'] = 'readonly'
#
# class AchievementForm(forms.ModelForm):
#     class Meta:
#         model = Achievement
#         fields = ['skater', 'competition', 'rank']

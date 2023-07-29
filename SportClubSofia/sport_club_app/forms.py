from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from SportClubSofia.sport_club_app.models import Skater

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'ala-bala'
            })
    )

    # class Meta(auth_forms.AuthenticationForm.Meta):


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'ala-bala'
            })
        }

    def save(self, commit=True):
        result = super().save(commit)
        return result


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }


class SkaterBaseForm(forms.ModelForm):
    class Meta:
        model = Skater
        fields = '__all__'
        # exclude = ('user',)


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

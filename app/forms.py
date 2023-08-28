from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        label = {"password1": "Password", "password2": "Conform Password"}
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"})}


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old Password"),
        strip=False,
        widget=forms.TextInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "class": "form-control",
            }
        ),
    )
    new_password1 = forms.CharField(
        label=_('New Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": 'new-password',
                "class":'form-control',
            }
        ),
        help_text= password_validation.password_validators_help_text_html()
    )

    new_password2 = forms.CharField(
        label=_('Conform Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": 'new-password',
                "class":'form-control',
            }
        )
    )

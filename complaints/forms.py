import email
from tkinter import Widget
from django import forms
import django
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Complainant,Complaint


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confirm Password(again)",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        labels = {"email":"Email"}
        widgets = {"username":forms.TextInput(attrs={"class":"form-control"})}


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs=
    {"autofocus":True, "class":"form-control"}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
    {"autocomplete":"current-password", "class" : "form-control"}))


class UserPasswordChange(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),
    strip=False,widget=forms.PasswordInput(attrs=
    {"autocomplete":"current-password","autofocus":True,
    "class":"form-control"}))
    new_password1 = forms.CharField(label=_("New Password"),
    strip=False,widget=forms.PasswordInput(attrs=
    {"autocomplete":"new-password","class":"form-control"}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),
    strip=False,widget=forms.PasswordInput(attrs=
    {"autocomplete":"new-password","autofocus":True,
    "class":"form-control"}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email',
        "class":"form-control"})
    )


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',"class":"form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',"class":"form-control"}),
    )


class UserPofileForm(forms.ModelForm):
    class Meta:
        model = Complainant
        fields=["first_name","last_name","street","city","postal_code"]
        widgets = {"first_name":forms.TextInput(attrs=
        {"class":"form-control"}),"last_name":forms.TextInput(attrs=
        {"class":"form-control"}), "street":forms.TextInput(attrs=
        {"class":"form-control"}), "city":forms.TextInput(attrs=
        {"class":"form-control"}), "postal_code":forms.TextInput(attrs=
        {"class":"form-control"})}


class UserComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields=["title","describe","category"]
        widgets = {
        "title":forms.TextInput(attrs={"class":"form-control"}),
        "describe":forms.TextInput(attrs={"class":"form-control"}),
        "category":forms.Select(attrs={"class":"form-control"})
        }
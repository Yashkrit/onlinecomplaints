from importlib.resources import path
from re import template
from unicodedata import name
from .forms import UserLoginForm,UserPasswordChange,MyPasswordResetForm,MySetPasswordForm

from django import views


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name="home"),
    path("registration/",views.UserRegistrationView.as_view(),name="registration"),
    
    path("accounts/login/",auth_views.LoginView.as_view(template_name="complaints/login.html",authentication_form=UserLoginForm),name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page="login"),name="logout"),
    
    path("profile/",views.ProfileView.as_view(),name="profile"),

    path("profile/address/",views.address,name="address"),

    path("complaint/",views.UserComplaintView.as_view(),name="complaint"),
    path("complaint/confirm/",views.allcomplaints,name="complaint_confirm"),
    path("complaint/registered/",views.complaintregistered,name="complaint_registered"),

    path("complaintstatus/",views.complaintstatus,name="complaintstatus"),
    
    path("changepassword/",auth_views.PasswordChangeView.as_view(template_name="complaints/changepassword.html",form_class = UserPasswordChange,success_url="/passwordchangedone/"),name="changepassword"),
    path("passwordchangedone/",auth_views.PasswordChangeDoneView.as_view(template_name="complaints/passwordchangedone.html"),name="passwordchangedone"),
    
    path("password-reset/",auth_views.PasswordResetView.as_view(template_name="complaints/password_reset.html",form_class=MyPasswordResetForm),name="password_reset"),
    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="complaints/password_reset_done.html"),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="complaints/password_reset_confirm.html",form_class=MySetPasswordForm),name="password_reset_confirm"),
    path("password-reset/complete/",auth_views.PasswordResetCompleteView.as_view(template_name="complaints/password_reset_complete.html"),name="password_reset_complete"),
]

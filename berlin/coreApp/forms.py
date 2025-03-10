from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address', 'password1', 'password2')


from django import forms

class CustomerForm(forms.Form):
    customer_fname = forms.CharField(max_length=200, label="First Name")
    customer_mname = forms.CharField(max_length=200, label="Middle Name", required=False)  # Middle name is optional
    customer_lname = forms.CharField(max_length=200, label="Last Name")
    customer_phone = forms.CharField(max_length=15, label="Phone Number")  # Use CharField for phone numbers
    customer_password1 = forms.CharField(max_length=200, label="Password", widget=forms.PasswordInput())
    customer_password2 = forms.CharField(max_length=200, label="Confirm Password", widget=forms.PasswordInput())
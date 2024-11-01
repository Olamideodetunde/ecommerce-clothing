from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control',
            'autocomplete': 'email'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control',
            'autocomplete': 'current-password'
        })
    )

class SignupForm(UserCreationForm):
  password1= forms.CharField(label='Enter Your Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
  password2=forms.CharField(label='Confirm Your Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Your Password'}))
  class Meta:
    model= User
    fields=('cust_fname','cust_lname', 'email', 'password1','password2')
    labels={'cust_lname':'Enter Your Last Name', 'cust_fname':'Enter Your First Name', 'cust_email':'Enter Your Email Address' }
    widgets = {
            'cust_lname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Last Name'}),
            'cust_fname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your First Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Your Email Address'}),
        }
  def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
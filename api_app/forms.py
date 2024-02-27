from django import forms 
from .models import User_Details

class SignupForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="E-mail")
    mobile = forms.IntegerField(label="Mobile No")
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput) 

class SigninForm(forms.Form):
    email = forms.EmailField(label="E-mail Address :")
    password = forms.CharField(label="Password :",widget=forms.PasswordInput)

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User_Details
        fields = ['first_name','last_name','email','mobile']
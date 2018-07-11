from django import forms
from first.models import Users

class NewUserForm(forms.ModelForm):
	class Meta:
		model=Users
		fields='__all__'
		widgets={'password':forms.PasswordInput(),}

class LoginForm(forms.Form):
	email=forms.CharField(required=True,label='Email',max_length=40)
	password=forms.CharField(required=True,label='Password',max_length=20,widget=forms.PasswordInput())

class SearchingForm(forms.Form):
	mysrc=forms.CharField(required=True,label='Source',max_length=40)
	mydest=forms.CharField(required=True,label='Destination',max_length=20)
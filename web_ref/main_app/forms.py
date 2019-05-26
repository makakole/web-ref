from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):


	# password2 = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

	class Meta:
		model = User
		fields = ['email', 'password1', 'password2']



        # password2 = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Repeat your password'}))



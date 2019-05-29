from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import IdData, References, RequestPermissions
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

User = get_user_model()

class UserRegisterForm(UserCreationForm):


	# password2 = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

	class Meta:
		model = User
		fields = ['email', 'password1', 'password2']



        # password2 = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Repeat your password'}))


class AddIdForm(forms.ModelForm):

	id_number = forms.CharField(required=True, max_length=13, label="ID Number")
	second_name = forms.CharField(required=False, help_text="Optional")

	class Meta:
		model = IdData
		fields = ('first_name', 'second_name', 'surname', 'id_number')

		def clean_title(self):
			return self.cleaned_data['first_name'].capitalize()

		widgets = {
            'first_name': forms.TextInput(attrs={'class': 'span8', 'id': 'basicinput', 'required': "required"}),
            'second_name': forms.TextInput(attrs={'class': 'span8', 'id': 'basicinput'}),
            'surname': forms.TextInput(attrs={'class': 'span8', 'id': 'basicinput', 'required': "required"}),
            'id_number': forms.TextInput(attrs={'class': 'span8', 'id': 'basicinput', 'required': "required"})
        }



class GenerateReferenceForm(forms.ModelForm):

	# expiry_date = forms.DateTimeField(required=False, help_text="Optional")

	class Meta:
		model = References
		fields = ['generated_for', 'reason', 'expiry_date']

		widgets = {
            'expiry_date': forms.TextInput(attrs={'type': 'date', 'class': 'span8', 'id': 'basicinput'})
        }


class RequestPermissionsForm(forms.ModelForm):

	class Meta:
		model = RequestPermissions
		fields = ['names', 'date_of_birth', 'gender', 'nationality', 'check_credit_score', 'check_criminal_record']
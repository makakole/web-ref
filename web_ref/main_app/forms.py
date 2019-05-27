from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import IdData

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

	def __init__(self, *args, **kwargs):
		# self.organizer = kwargs.pop('organizer')
		super(AddIdForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['first_name'].initial = 'jnljnk'#self.organizer.default_location
			# self.fields['required'].widget = CheckboxInput(required=False)
	def clean_time(self):
		surname = self.cleaned_data['surname'].upper()
    #     # do stuff with the time to put it in UTC based on the user's default timezone and data passed into the form.

    # def save(self, *args, **kwargs):
    #     self.instance.organizer = self.organizer
    #     meal = super(MealForm, self).save(*args, **kwargs)
    #     return meal

		widgets = {
            'first_name': forms.TextInput(attrs={'class': 'span8', 'id': 'basicinput', 'required': "required"}),
            'second_name': forms.TextInput(attrs={'class': 'span8', 'id': 'basicinput'}),
            'surname': forms.TextInput(attrs={'class': 'span8', 'id': 'basicinput', 'required': "required"}),
            'id_number': forms.TextInput(attrs={'class': 'span8', 'id': 'basicinput', 'required': "required"})
        }



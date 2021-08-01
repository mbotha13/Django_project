from django import forms
from django.forms import ModelForm
from .models import Johannesburg_booking





class add_bookingForm(ModelForm):
	class Meta:
		model = Johannesburg_booking
		fields =('bootcamp_type','email', 'bootcamp_month', 'camp_date',)
		labels ={
			'email':'',
			'bootcamp_type':'',
			'bootcamp_month': '',
			'camp_date': '',

		}
		widgets = {
			'bootcamp_type': forms.RadioSelect(attrs={'class':'form-control',}),
			'email': forms.EmailInput(attrs= {'class':'form-control','placeholder':'email'}),
			'bootcamp_month':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'boot-camp-month'}),
			'camp_date':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'boot camp date'})


		}
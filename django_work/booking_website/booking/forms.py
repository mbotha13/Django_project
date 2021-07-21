from django import forms
from django.forms import ModelForm
from .models import booking





class update_bookingForm(ModelForm):
	class Meta:
		model = booking
		fields =('bootcamp_type','name', 'bootcamp_month', 'camp_date')
		labels ={
			'name': '',
			'bootcamp_type':'',
			'bootcamp_month': '',
			'camp_date': '',

		}
		widgets = {
			'bootcamp_type': forms.RadioSelect(attrs={'class':'form-control',}),
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'username'}),
			'bootcamp_month':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'boot-camp-month'}),
			'camp_date':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'boot camp date'})


		}
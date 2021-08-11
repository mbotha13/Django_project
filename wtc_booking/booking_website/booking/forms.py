from django import forms
from django.forms import ModelForm
from .models import Johannesburg_booking,Date,Month,Cape_Town_booking,Durban_booking
from booking.models import Johannesburg_booking, Date




class add_bookingForm(forms.ModelForm):
	class Meta:
		model = Johannesburg_booking
		fields =('bootcamp_type', 'date',)
		
		widgets = {
		'bootcamp_type' : forms.RadioSelect(attrs={'class' : 'form-check form-check-inline',}),
		'date' :forms.Select(attrs={'class' : 'form-control',}),
		}

	


class CapeBookingForm(forms.ModelForm):
	class Meta:
		model = Cape_Town_booking
		fields =('bootcamp_type', 'date',)

		widgets = {
		'bootcamp_type' : forms.RadioSelect(attrs={'class' : 'form-control',}),
		'date' :forms.Select(attrs={'class' : 'form-control',}),
		}
		


class DurbanBookingForm(forms.ModelForm):
	class Meta:
		model = Durban_booking
		fields =('bootcamp_type', 'date',)

		widgets = {
		'bootcamp_type' : forms.RadioSelect(attrs={'class' : 'form-control',}),
		'date' :forms.Select(attrs={'class' : 'form-control',}),
		}
		
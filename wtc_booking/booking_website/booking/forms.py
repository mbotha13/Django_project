from django import forms
from django.forms import ModelForm
from .models import Johannesburg_booking,Date,Month,Cape_Town_booking,Durban_booking
from booking.models import Johannesburg_booking, Date




<<<<<<< HEAD

class add_bookingForm(forms.ModelForm):
	class Meta:
		model = Johannesburg_booking
		fields =('bootcamp_type', 'month', 'date',)
		

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['date'].queryset = Date.objects.none()

			if 'month' in self.data:
				try:
					month_id = int(self.data.get(month))
					self.fields['date'].queryset = Date.objects.filter(month_id=month_id).order_by('name')
				except (ValueError, TypeError):
					pass
			elif self.instance.pk:
				self.fields['date'].queryset = self.instance.month.date_set.order_by('name')
=======
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
		
>>>>>>> 1a6facb7e71889a5a99a011a1df96316abc880c1

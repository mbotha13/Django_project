from django import forms
from django.forms import ModelForm
from .models import Johannesburg_booking





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
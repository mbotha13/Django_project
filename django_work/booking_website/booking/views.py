from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from .models import booking
from .forms import update_bookingForm

# Create your views here.
def update_booking(request):
	submitted = False
	if request.method == "POST":
		form = update_bookingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/update_booking?submitted=True')
	else:
		form = update_bookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking/update_booking.html', {'form':form, 'submitted':submitted})

def booking_form(request):
	form = BookingForm
	return render(request, 'booking/booking_form.html', {'form':form,})

def home(request, year, month):
	month = month.title()
	#Convert manth from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)


	cal =HTMLCalendar().formatmonth(year,month_number)


	return render(request, 'booking/home.html',{
		"year": year,
		"month": month,
		"month_number": month_number,
		"cal":cal,
		})
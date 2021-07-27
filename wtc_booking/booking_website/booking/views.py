from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Johannesburg_booking
from .forms import add_bookingForm

# Create your views here.
def home(request):
	submitted = False
	if request.method == "POST":
		form = add_bookingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_booking?submitted=True')
	else:
		form = add_bookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})
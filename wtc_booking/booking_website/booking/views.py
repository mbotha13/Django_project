from django.shortcuts import render
from django.http import HttpResponseRedirect
<<<<<<< HEAD
from .models import Johannesburg_booking, Date
from .forms import add_bookingForm 

# Create your views here.
=======
from .models import Johannesburg_booking, Date, Month,Durban_booking,Cape_Town_booking
from .forms import add_bookingForm, CapeBookingForm, DurbanBookingForm

# Create your views here.

>>>>>>> 1a6facb7e71889a5a99a011a1df96316abc880c1
def booking_page(request):
	submitted = False
	if request.method == "POST":
		form = add_bookingForm(request.POST)
		if form.is_valid():
			user_info = form.save(commit=False)
			user_info.user= request.user
			user_info.save()


			return HttpResponseRedirect('/add_booking?submitted=True')
	else:
		form = add_bookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})


<<<<<<< HEAD
def load_date(request):
	month_id = request.GET.get('month_id')
	date = Date.objects.filter(month_id=month_id)
	return render(request,'booking_page/date_dropdown.html', {'date':date})
	#return JsonResponse(list(date.values('id', 'name')), safe = False)
=======
def DurbanBookingPage(request):
	submitted = False
	if request.method == "POST":
		form = DurbanBookingForm(request.POST)
		if form.is_valid():
			user_info = form.save(commit=False)
			user_info.user= request.user
			user_info.save()


			return HttpResponseRedirect('/DurbanBooking?submitted=True')
	else:
		form = DurbanBookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})


def CapeBookingPage(request):
	submitted = False
	if request.method == "POST":
		form = CapeBookingForm(request.POST)
		if form.is_valid():
			user_info = form.save(commit=False)
			user_info.user= request.user
			user_info.save()


			return HttpResponseRedirect('/CapeBooking?submitted=True')
	else:
		form = CapeBookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})
>>>>>>> 1a6facb7e71889a5a99a011a1df96316abc880c1

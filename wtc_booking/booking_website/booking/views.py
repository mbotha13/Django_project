from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Johannesburg_booking, Date, Month,Durban_booking,Cape_Town_booking
from .forms import add_bookingForm, CapeBookingForm, DurbanBookingForm
import csv

# Create your views here.
def GetCsv(request):
	response = HttpResponse(content_type='text/csv')
	response['content-Discription'] = 'attachment; filename="bookings.csv"'
	writer = csv.writer(response)
	writer.writerow(['campus', 'user', 'bootcamp_type', 'date'])
	Jbookings = Johannesburg_booking.objects.all()
	Cbookings = Cape_Town_booking.objects.all()
	Dbookings = Durban_booking.objects.all()

	for Jbooking in Jbookings:
		writer.writerow(['Johannesburg',Jbooking.user, Jbooking.bootcamp_type, Jbooking.date])
	for Cbooking in Cbookings:
		writer.writerow(['Cape_Town',Cbooking.user, Cbooking.bootcamp_type, Cbooking.date])
	for Dbooking in Dbookings:
		writer.writerow(['Durban',Dbooking.user, Dbooking.bootcamp_type, Dbooking.date])

	return response


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

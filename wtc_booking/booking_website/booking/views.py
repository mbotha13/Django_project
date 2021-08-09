from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from booking.models import Johannesburg_booking, Date, Month,Durban_booking,Cape_Town_booking
from .forms import add_bookingForm, CapeBookingForm, DurbanBookingForm
import csv

# Create your views here.

def JohannesburgCancelation(request):
	if Johannesburg_booking.objects.filter(user = request.user).exists():
		booking = Johannesburg_booking.objects.get(user = request.user)

	elif Cape_Town_booking.objects.filter(user = request.user).exists():
		booking = Cape_Town_booking.objects.get(user = request.user)
		
	else:
		booking = Durban_booking.objects.get(user =request.user)
	booking.delete()
	return redirect('/add_booking')

def CapeCancelation(request):
	if Cape_Town_booking.objects.filter(user = request.user).exists():
		booking = Cape_Town_booking.objects.get(user = request.user)

	elif Durban_booking.objects.filter(user = request.user).exists():
		booking = Durban_Town_booking.objects.get(user = request.user)
		
	else:
		booking = Johannesburg_booking.objects.get(user =request.user)
	booking.delete()
	return redirect('/add_booking')


def DurbanCancelation(request):
	if Durban_booking.objects.filter(user = request.user).exists():
		booking = Durban_booking.objects.get(user = request.user)

	elif Cape_Town_booking.objects.filter(user = request.user).exists():
		booking = Cape_Town_booking.objects.get(user = request.user)
		
	else:
		booking = Johannesburg_booking.objects.get(user =request.user)
	booking.delete()
	return redirect('/add_booking')


def JohannesburgReschedule(request):
	submitted = False
	booking = Johannesburg_booking.objects.get(user = request.user)
	form = add_bookingForm(request.POST or None, instance= booking)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/add_booking?submitted=True')
	else:
		form = CapeBookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking_page/update_booking.html', {'form':form, 'booking':booking, 'submitted':submitted})


def CapeReschedule(request):
	submitted = False
	booking = Cape_Town_booking.objects.get( user = request.user)
	form = CapeBookingForm(request.POST or None, instance= booking)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/CapeBooking?submitted=True')
	else:
		form = CapeBookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking_page/update_booking.html', {'form':form, 'booking': booking, 'submitted':submitted})


def DurbanReschedule(request):
	submitted = False
	booking = Durban_booking.objects.get(user = request.user)
	form = DurbanBookingForm(request.POST or None, instance= booking)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/DurbanBooking?submitted=True')
	else:
		form = DurbanBookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking_page/update_booking.html', {'form':form, 'booking': booking, 'submitted':submitted})



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



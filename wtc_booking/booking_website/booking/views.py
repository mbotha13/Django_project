from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect,HttpResponse
from booking.models import Johannesburg_booking, Date, Month,Durban_booking,Cape_Town_booking
from .forms import add_bookingForm, CapeBookingForm, DurbanBookingForm
from django.template.loader import render_to_string
from django.conf import settings
import csv
import smtplib
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
		booking = Durban_booking.objects.get(user = request.user)
		
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

		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				campus = 'Johannesburg'
    
				smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASS)
				template = render_to_string('booking_page/reschedule_email.html',{'name':request.user.username, 'campus':campus, 'booking':booking})
				subject = 'WTC Bootcamp Booking Rescheduled'
				message = f'Hello {request.user.username}, Your Booking has been confirmed'
				msg = f'Subject: {subject}\n\n{template}'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [request.user.email,]
				smtp.sendmail(email_from, recipient_list, msg)
		return HttpResponseRedirect('/add_booking?submitted=True')
	else:
		form = add_bookingForm
		if 'submitted' in request.GET:
			submitted = True

			
	return render(request, 'booking_page/update_booking.html', {'form':form, 'booking':booking, 'submitted':submitted})


def CapeReschedule(request):
	submitted = False
	booking = Cape_Town_booking.objects.get( user = request.user)
	form = CapeBookingForm(request.POST or None, instance= booking)
	if form.is_valid():
		form.save()
		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				campus = 'Cape_Town'
    
				smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASS)
				template = render_to_string('booking_page/reschedule_email.html',{'name':request.user.username, 'campus':campus, 'booking':booking})
				subject = 'WTC Bootcamp Booking Confirmation'
				message = f'Hello {request.user.username}, Your Booking has been confirmed'
				msg = f'Subject: {subject}\n\n{template}'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [request.user.email,]
				smtp.sendmail(email_from, recipient_list, msg)
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

		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				campus = 'Durban'
    
				smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASS)
				template = render_to_string('booking_page/reschedule_email.html',{'name':request.user.username, 'campus':campus, 'booking':booking})
				subject = 'WTC Bootcamp Booking Confirmation'
				message = f'Hello {request.user.username}, Your Booking has been confirmed'
				msg = f'Subject: {subject}\n\n{template}'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [request.user.email,]
				smtp.sendmail(email_from, recipient_list, msg)
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

			booking = Johannesburg_booking.objects.get(user = request.user)

			with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				campus = 'Johannesburg'
    
				smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASS)
				template = render_to_string('booking_page/email_template.html',{'name':request.user.username, 'booking':booking, 'campus':campus})
				subject = 'WTC Bootcamp Booking Confirmation'
				message = f'Hello {request.user.username}, Your Booking has been confirmed'
				msg = f'Subject: {subject}\n\n{template}'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [request.user.email,]
				smtp.sendmail(email_from, recipient_list, msg)


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

			booking = Durban_booking.objects.get(user = request.user)

			with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				campus = 'Durban'
    
				smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASS)
				template = render_to_string('booking_page/email_template.html',{'name':request.user.username, 'booking':booking, 'campus':campus})
				subject = 'WTC Bootcamp Booking Confirmation'
				message = f'Hello {request.user.username}, Your Booking has been confirmed'
				msg = f'Subject: {subject}\n\n{template}'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [request.user.email,]
				smtp.sendmail(email_from, recipient_list, msg)


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

			booking = Cape_Town_booking.objects.get( user = request.user)

			with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				campus = 'Cape town'
    
				smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASS)
				template = render_to_string('booking_page/email_template.html',{'name':request.user.username, 'booking':booking, 'campus':campus})
				subject = 'WTC Bootcamp Booking Confirmation'
				message = f'Hello {request.user.username}, Your Booking has been confirmed'
				msg = f'Subject: {subject}\n\n{template}'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [request.user.email,]
				smtp.sendmail(email_from, recipient_list, msg)
			return HttpResponseRedirect('/CapeBooking?submitted=True')
	else:
		form = CapeBookingForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'booking_page/add_booking.html', {'form':form, 'submitted':submitted})



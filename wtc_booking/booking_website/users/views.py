from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from booking.models import Johannesburg_booking, Date, Month,Durban_booking,Cape_Town_booking


# Create your views here.

def home(request):
    return render(request,'users/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()


    return render(request,'users/register.html', {'form':form})


@login_required()
def user_profile(request):
    if Johannesburg_booking.objects.filter(user = request.user).exists():
        bookings = Johannesburg_booking.objects.get(user = request.user)
        campus = 'Johannesburg'

    elif Cape_Town_booking.objects.filter(user = request.user).exists():
        bookings = Cape_Town_booking.objects.get(user = request.user)
        campus = 'Cape_Town'
        
    elif Durban_booking.objects.filter(user = request.user).exists():
        bookings = Durban_booking.objects.get(user =request.user)
        campus = 'Durban'
    else:
        bookings = 'None'
        campus = 'None'
    return render(request, 'users/user_profile.html',{'bookings':bookings, 'campus':campus})
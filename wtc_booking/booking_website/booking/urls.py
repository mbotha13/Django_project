
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name="booking_page"),
    path('add_booking', views.booking_page, name='add_booking'),
    path('CapeBooking', views.CapeBookingPage, name='CapeBooking'),
    path('DurbanBooking', views.DurbanBookingPage, name='DurbanBooking'),
  
]

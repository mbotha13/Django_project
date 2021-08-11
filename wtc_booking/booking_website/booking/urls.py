from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name="booking_page"),
    path('add_booking', views.booking_page, name='add_booking'),
    path('CapeBooking', views.CapeBookingPage, name='CapeBooking'),
    path('DurbanBooking', views.DurbanBookingPage, name='DurbanBooking'),
    path('get_csv', views.GetCsv, name='get_csv'),
    path('JohannesburgReschedule',views.JohannesburgReschedule, name='JohannesburgReschedule'),
    path('CapeReschedule',views.CapeReschedule, name='CapeReschedule'),
    path('DurbanReschedule',views.DurbanReschedule, name='DurbanReschedule'),
    path('JohannesburgCancelation',views.JohannesburgCancelation, name='JohannesburgCancelation'),
    path('CapeCancelation',views.CapeCancelation, name='CapeCancelation'),
    path('DurbanCancelation',views.DurbanCancelation, name='DurbanCancelation'),

    
]

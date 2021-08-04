
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name="booking_page"),
    path('add_booking', views.booking_page, name='add_booking'),
<<<<<<< HEAD

    path('ajax/load-date/', views.load_date, name = 'ajax_load_date'),
=======
    path('CapeBooking', views.CapeBookingPage, name='CapeBooking'),
    path('DurbanBooking', views.DurbanBookingPage, name='DurbanBooking'),
  
>>>>>>> 1a6facb7e71889a5a99a011a1df96316abc880c1
]

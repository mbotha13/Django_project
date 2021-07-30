from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name="booking_page"),
    path('add_booking', views.booking_page, name='add_booking'),

    path('ajax/load-date/', views.load_date, name = 'ajax_load_date'),
]

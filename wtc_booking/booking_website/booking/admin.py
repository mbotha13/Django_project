from django.contrib import admin
from .models import Johannesburg_booking,Cape_Town_booking,Durban_booking,Month,Date
import csv
from django.http import HttpResponse
# Register your models here.




class JohannesburgAdmin(admin.ModelAdmin):
	list_display = ['user', 'bootcamp_type', 'date']
	


admin.site.register(Johannesburg_booking,JohannesburgAdmin)
admin.site.register(Cape_Town_booking)
admin.site.register(Durban_booking)
admin.site.register(Month)
admin.site.register(Date)  
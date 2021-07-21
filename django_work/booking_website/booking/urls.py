from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('<int:year>/<str:month>/', views.home, name="home"),
    path('update_booking', views.update_booking, name='update_booking')
]
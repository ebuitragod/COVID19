#api.urls.py
from django.urls import include, path
from rest_framework import routers

from api import views

urlpatterns = [
	path('all/', views.LocationList ),
	path('load/', views.LocationLoad )
]
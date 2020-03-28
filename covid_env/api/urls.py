#api.urls.py
from django.urls import include, path
from rest_framework import routers

from api import views

urlpatterns = [
	path('all/', views.LocationListView.as_view() ),
	path('load/', views.LocationLoad )
]
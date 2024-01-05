from django.urls import path

from . import views

urlpatterns = [
    path('contacts', views.contacts, name='contacts') # ensure it is included in the main urls.py
]
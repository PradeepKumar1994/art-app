from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ContactUs.as_view(), name='contact-page')
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Gallery.as_view(), name = 'gallery-page')
]

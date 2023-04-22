from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    def get(self, request):
        return render(request, 'home.html')
from django.urls import path
from .views import home_page_view

#Create your views here

def home_page_view(request):
    return HttpResponse("This is the home page")

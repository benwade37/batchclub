from django.urls import path
from .views import home_page_view

from django.urls import path
from .views import profile_view

urlpatterns = [
    path('',home_page_view, name='home'),
    path('profile/', profile_view, name='profile')
]

from django.urls import path
from .views import about, contact, home

urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('contact/', contact)

]

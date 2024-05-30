from django.urls import path
from .views import about, contact, home,view_color

urlpatterns = [
    path('home/<str:color_type>/', home, name='blog-home'),
    path('home/', home, name='blog-home-without-color'),
    path('about/<str:color_type>', about, name='blog-about'),
    path('about/', about, name='blog-about-without-color'),
    path('contact/', contact, name='blog-contact'),
    path('color/<str:color_type>/', view_color, name='blog-color')

]

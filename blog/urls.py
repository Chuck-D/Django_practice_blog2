from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name= 'blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    #path('user/register', views.register, name='user-register')
]

from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('blog.html', views.blog, name="blog"),
    path('service.html', views.service, name="service"),
    path('contact.html', views.contact, name="contact"),
]
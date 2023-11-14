from django.urls import path

from .views import HomeView, about, skill_view, contact

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('skill/', skill_view, name='skill'),
    path('contact/', contact, name='contact'),
]

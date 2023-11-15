from django.urls import path

from .views import HomeView, about, skill_view, contact_view, SkillDetailView, contact_success_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('skill/', skill_view, name='skill'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact-sucess'),
    path('skill/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
]

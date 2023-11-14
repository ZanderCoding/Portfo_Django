from django.urls import path

from .views import HomeView, about, skill_view, contact, SkillDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('skill/', skill_view, name='skill'),
    path('contact/', contact, name='contact'),
    path('skill/<int:pk>', SkillDetailView.as_view(), name='skill-detail'),
]

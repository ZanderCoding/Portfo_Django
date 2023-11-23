from django.urls import path

from .views import HomeView, About, skill_view, contact_view, SkillDetailView, contact_success_view, projects_page

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('skill/', skill_view, name='skill'),
    path('projects/', projects_page, name='projects-page'),
    path('contact/', contact_view, name='contact'),
    path('success/', contact_success_view, name='contact-sucess'),
    path('skill/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
]

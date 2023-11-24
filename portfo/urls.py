from django.urls import path

from .views import HomeView, About, skill_view, contact_view, SkillDetailView, contact_success_view, project_view, ProjectDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('skill/', skill_view, name='skill'),
    path('projects/', project_view, name='projects-page'),
    path('contact/', contact_view, name='contact'),
    path('success/', contact_success_view, name='contact-sucess'),
    path('skill/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]

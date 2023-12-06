from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, DetailView
from .forms import ContactForm

from .models import Skill, Project
# Create your views here.


class HomeView(TemplateView):
    template_name = "portfo/index.html"


class About(TemplateView):
    template_name = 'portfo/about.html'


def skill_view(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'portfo/skill_view.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-sucess')
    else:
        form = ContactForm()
    contex = {
        'form': form
    }
    return render(request, 'portfo/contact.html', contex)


def contact_success_view(request):
    return render(request, 'portfo/contact_success.html')


class SkillDetailView(DetailView):
    model = Skill


def project_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfo/projects_page.html', context)


class ProjectDetailView(DetailView):
    model = Project


class ResumeView(TemplateView):
    template_name = 'portfo/resume.html'

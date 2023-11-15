from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, DetailView
from .forms import ContactForm

from .models import Skill
# Create your views here.


class HomeView(TemplateView):
    template_name = "portfo/index.html"


def about(request):
    return HttpResponse('<h1>About</h1>')


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
            return redirect('/contact/success/')
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


def projects_page(request):
    return render(request, 'portfo/projects_page.html')

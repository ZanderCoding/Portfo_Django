from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView, DetailView
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


def contact(request):
    return HttpResponse('<h1>You can contact me here in the future</h1>')


class SkillDetailView(DetailView):
    model = Skill

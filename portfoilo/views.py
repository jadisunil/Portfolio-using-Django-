from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, About, WorkExperience, Contact

# Create your views here.


def home(request):
    about = About.objects.first()
    projects = Project.objects.all()
    contact = Contact.objects.first()
    experiences = WorkExperience.objects.all()
    return render(request, 'indes.html', {
        'about': about,
        'projects': projects,
        'contact': contact,
        'experiences': experiences
    })

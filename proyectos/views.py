from django.shortcuts import render
from .models import Project

def proyectos(request):
    projects = Project.objects.all()
    return render(request, "proyectos/projects.html",
    {'projects':projects})

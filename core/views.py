from django.shortcuts import render

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def skills(request):
    return render(request, "core/skills.html")

def projects(request):
    return render(request, "core/projects.html")

def estudiando(request):
    return render(request, "core/estudiando.html")

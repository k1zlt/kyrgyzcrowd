from django.shortcuts import render
from .models import Project

# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/project_detail.html', {
        'project': project
    })
    
def new_project(request, slug):
    pass
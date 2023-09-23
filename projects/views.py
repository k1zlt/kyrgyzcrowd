from django.shortcuts import render
from .models import Project, Category

# Create your views here.
def all_projects(request):
    return render(request, 'projects/projects.html', {
        'projects': Project.objects.all(),
        'categories' : Category.objects.all()
    })

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/project_detail.html', {
        'project': project
    })
    
def category(request, slug):
    pass
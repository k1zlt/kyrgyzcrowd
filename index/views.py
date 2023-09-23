from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index/index.html')

def projects(request):
    return render(request, 'index/projects.html')

def best(request):
    return render(request, 'index/best.html')

def about(request):
    return render(request, 'index/about.html')

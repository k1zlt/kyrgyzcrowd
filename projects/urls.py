from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path("", views.all_projects, name='all_projects'),
    path("<slug:slug>/", views.project_detail, name='project_detail'),
    path("new/", views.new_project, name='new_project')
]

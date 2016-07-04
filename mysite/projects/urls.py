from django.conf.urls import url, patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'projects'
urlpatterns = [
    url(r'^create/$', views.CreateProjectView.as_view(), name="project_create"),
    #url(r'^create/$', views.project_create, name="project_create"),
    url(r'^$', views.IndexView.as_view(), name="projectslist"),
    #url(r'^$', views.projectslist, name="projectslist"),
]

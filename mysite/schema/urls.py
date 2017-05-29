from django.conf.urls import url, patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from . import views
import users

urlpatterns = [
    url(r'^show_schema$', views.ShowSchemaView.as_view(), name='schema'),
    url(r'^create$', views.CreateChoiceView.as_view(), name = 'create'),
    url(r'^delete$', views.DeleteChoiceView.as_view(), name = 'delete'),
    url(r'^reset$', views.ResetChoicesView.as_view(), name = 'reset'),
]

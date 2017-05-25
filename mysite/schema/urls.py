from django.conf.urls import url, patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from . import views
import users

urlpatterns = [
    url(r'^show_schema$', TemplateView.as_view(template_name="show_schema.html"), name='schema'),
]

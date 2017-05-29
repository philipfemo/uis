from django.shortcuts import render
from django.template import RequestContext
from schema.views import ShowSchemaView


def index(request):
    return render(request, "index.html")

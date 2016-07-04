from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
#from .models import Choice, Question
from django.utils.decorators import method_decorator
from .models import Project
from .forms import ProjectForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
# Create your views here.
@method_decorator(login_required(login_url = "/login"), name = "dispatch")
class CreateProjectView(FormView):
    template_name = "project_form.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("projects:projectslist")

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        project = form.save(commit=False)
        project.author = self.request.user
        project.save()

        return super(CreateProjectView, self).form_valid(form)

@method_decorator(login_required(login_url = "/login"), name = "dispatch")
class IndexView(ListView):
    model = Project
    template_name = "projectslist.html"

#def projectslist(request):
#    projects = Project.objects.all()
#    context = {
#        "objects_list": projects,
#        "title": "List"
#    }
#    return render(request, "projectslist.html", context)

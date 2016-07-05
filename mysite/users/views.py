from .forms import LoginForm, UserForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView
from django.utils.decorators import method_decorator

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def get_success_url(self):
        return reverse("home")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            login(self.request, user)
        return super(LoginView, self).form_valid(form)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

class IndexView(ListView):
    model = User
    template_name = "user_list.html"

class CreateUserView(FormView):
    template_name = "create_user.html"
    form_class = UserForm
    #object_name = "user_data"


    def get_success_url(self):
        return reverse("users:user_list")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        password = form.cleaned_data["password"]
        faculty = form.cleaned_data["faculty"]
        study = form.cleaned_data["study"]
        roles = form.cleaned_data["roles"]


        User.objects.create_user(
            email,
            first_name,
            last_name,
            faculty,
            study,
            roles,
            password = password
        )

        return super(CreateUserView, self).form_valid(form)

class UpdateUserView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "create_user.html"
    object_template_name = "user_data"
    success_url = "/users/list"

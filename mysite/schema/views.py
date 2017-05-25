from django.shortcuts import render
from users.forms import LoginForm, UserForm
from users.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView
from django.utils.decorators import method_decorator

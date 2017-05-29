from django.shortcuts import render
from users.forms import LoginForm, UserForm
from users.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic import View, TemplateView
from django.utils.decorators import method_decorator
from .models import Choice, SlotField

class CreateChoiceView(View):
    def post(self, request, *args, **kwargs):
        slot_id = request.POST.get("slot_id")
        Choice.objects.create(slot_id=slot_id, owner=request.user)
        return HttpResponseRedirect(reverse('schemas:schema'))

class DeleteChoiceView(View):
    def post(self, request, *args, **kwargs):
        slot_id = request.POST.get("slot_id")
        Choice.objects.filter(slot_id=slot_id, owner=request.user).delete()
        return HttpResponseRedirect(reverse('schemas:schema'))

class ResetChoicesView(View):
    def post(self, request, *args, **kwargs):
        Choice.objects.all().delete()
        return HttpResponseRedirect(reverse('schemas:schema'))

class ShowSchemaView(TemplateView):
    template_name = 'show_schema.html'

    def get_context_data(self, **kwargs):
       context = super(ShowSchemaView, self).get_context_data(**kwargs)
       context['monday_slots'] = SlotField.objects.filter(day="mon")
       context['thursday_slots'] = SlotField.objects.filter(day="thu")
       context['has_booked_monday'] = Choice.objects.filter(owner=self.request.user, slot__day = "mon").exists()
       context['has_booked_thursday'] = Choice.objects.filter(owner=self.request.user, slot__day = "thu").exists()
       return context

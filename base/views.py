from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from .models import Action
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields = '__all__'
    redirect_authenticated_user= True

    def get_success_url(self):
        return reverse_lazy('actions')



# Create your views here.
class ActionList(LoginRequiredMixin,ListView):
    model=Action
    context_object_name= 'actions'


class ActionDetail(LoginRequiredMixin, DetailView):
    model=Action
    context_object_name='action'
    template_name='base/action.html'

class ActionCreate(LoginRequiredMixin ,CreateView):
    model=Action
    fields= '__all__'
    success_url= reverse_lazy('actions')

    
class ActionUpdate(LoginRequiredMixin , UpdateView):
    model=Action
    fields= '__all__'
    success_url= reverse_lazy('actions')
    

class DeleteView(LoginRequiredMixin, DeleteView):
    model=Action
    context_object_name='action'
    success_url= reverse_lazy('actions')
   

   
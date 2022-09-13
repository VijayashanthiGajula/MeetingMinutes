from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView,FormView
from .models import Action
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields = '__all__'
    redirect_authenticated_user= True

    def get_success_url(self):
        return reverse_lazy('actions')

class RegisterPage(FormView):
    template_name='base/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url = reverse_lazy('actions')

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

# Create your views here.
class ActionList(LoginRequiredMixin,ListView):
    model=Action
    context_object_name= 'actions'

    #user gets only thier corresponding databases
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['actions']= context['actions'].filter(user=self.request.user)
        context['count']= context['actions'].filter(complete=False).count()
        return context


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
   

   
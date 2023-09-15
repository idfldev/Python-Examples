# from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy # if you want to redirect to a different page, you can
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login-page')
        context = {'form': form}
        return render(request, "Authenticated/register.html", context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username or password is incorrect")
            # return render(request, "staff/login.html", context)
    context = {}
    return render(request, "Authenticated/login.html", context)


# def logoutPage(request):
#     logout(request)
#     return redirect('home')


# Create your views here.
# @login_required(login_url='home')
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'Dashboard/dashboard.html', {}) 
    else:
        return render(request, 'Authenticated/block_page.html', {})

# @login_required(login_url='home')
def audit(request):
    if request.user.is_authenticated:
        return render(request, 'Dashboard/Audit/auditor.html', {}) 
    else:
        return redirect('home')
    

# @login_required(login_url='home')
def cs(request):
    if request.user.is_authenticated:
        return render(request, 'Dashboard/CS/cs.html', {})
    else:
        return redirect('home')


# @login_required(login_url='home')
def inspection(request):
    if request.user.is_authenticated:
        return render(request, 'Dashboard/Inspection/inspector.html', {})
    else:
        return redirect('home')
    

# --------------------------------------------------
class CustomLoginView(LoginView):
    template_name = 'staff/login.html'
    fields = '__all__'
    # form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)	
        context['count'] = context['tasks'].filter(complete=False).count()	
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    # template_name = 'staff/task.html' # if you want custom template from html file


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # field = ['title', 'description']  # optional field
    fields = ['title', 'desciption']                  # get all fields to show in your form
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'desciption']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

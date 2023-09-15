from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home/home.html', {})

def testing(request):
    return render(request, 'Home/testing.html', {})

def audit(request):
    return render(request, 'Home/audit.html', {})

def application_form(request):
    return render(request, 'Forms/form_GRS_RCS.html', {})

def dashboard(request):
    return render(request, 'Users/index.html', {})





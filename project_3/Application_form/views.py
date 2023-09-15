from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'Home/home.html', {})

def homeTesting(request):
    return render(request, 'Home/testing.html', {})

def homeAudit(request):
    return render(request, 'Home/audit.html', {})

def application_form(request):
    return render(request, 'Home/application_form.html', {})

def grsRcs(request):
    return render(request, 'Home/Forms/GRS_RCS.html', {})

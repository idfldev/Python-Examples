from django.shortcuts import render, HttpResponse
from .pdf import html2pdf


# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def pdfPage(request):
    pdf = html2pdf("pdf.html")
    # return render(request, 'pdf.html',{})
    return HttpResponse(pdf, content_type='application/pdf')
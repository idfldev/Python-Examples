from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# def html2pdf(template_sources, context_dict={}):
#     template = get_template(template_sources)
#     html = template.render(context_dict)
#     result = BytesIO()
#     # UFT-8 => encode method
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result, encoding='utf-8')
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None

# pisaStatus = pisa.CreatePDF(
#     StringIO(sourceHtml.encode('utf-8')),                 
#     dest=resultFile,
#     encoding='utf-8')

# def html2pdf(template_sources, context_dict=None):
#     if context_dict is None:
#         context_dict = {}

#     template = get_template(template_sources)
#     html = template.render(context_dict)

#     result = BytesIO()
#     try:
#         # Encoding and replacing unsupported characters with '?'
#         pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8", "replace")), result)
#     except (UnicodeEncodeError, UnicodeDecodeError):
#         return None

#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')

#     return None


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def html2pdf(template_sources, context_dict=None):
    if context_dict is None:
        context_dict = {}

    template = get_template(template_sources)
    html = template.render(context_dict)

    result = BytesIO()
    try:
        # Encoding and decoding using utf-8 to handle Unicode characters
        pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    except (UnicodeEncodeError, UnicodeDecodeError):
        return None

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    return None

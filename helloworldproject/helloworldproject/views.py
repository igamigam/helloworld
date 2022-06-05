from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnobject = HttpResponse('HELLO WORLD')
    return  returnobject

class HelloworldView(TemplateView):
    template_name = 'hello.html'
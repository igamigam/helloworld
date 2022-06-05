from django.http import HttpResponse

def helloworldfunction(request):
    returnobject = HttpResponse('HELLO WORLD')
    return  returnobject
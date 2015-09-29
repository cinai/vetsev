from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response

def hogar(request):
    return render_to_response('index.html',{'navbar':'navbar.html','template_included':'caja.html'},)

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world_view(request):
    return render(request, 'index.html')

def hello_world_http_response(request):
    return HttpResponse("Hello world from HttpResponse")
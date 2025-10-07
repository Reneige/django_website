from django.shortcuts import render
from django.http import HttpResponse

def test_response(request):
    return HttpResponse('Test Successful')

def render_projects(request):
    return render(request, 'projects.html')

def render_about_me(request):
    return render(request, 'about_me.html')

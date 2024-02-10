from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'home.html', {'name': 'Juan Esteban Barrios'})
def about (request):
    return HttpResponse('<h1>Welcome to about page</h1>')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def comun(request):
    return render(request, 'comun.html')
def index(request):
    return render(request, 'index.html')

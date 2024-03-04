from django.shortcuts import render
from.models import Egresado

# Create your views here.
def egresado(request):
    egresados = Egresado.objects.all()
    return render(request, 'egresado/egresado.html', {'egresados': egresados})
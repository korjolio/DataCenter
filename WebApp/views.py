from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'WebApp/home.html')

@login_required
def tienda(request):
    return render(request, 'WebApp/tienda.html')

def contacto(request):
    return render(request, 'WebApp/contacto.html')

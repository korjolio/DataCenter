from django.shortcuts import render
from .forms import CustomUserForm, PedidoForm, ContactoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Pedido
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework import viewsets
from .serializers import PedidoSerializer

# Create your views here.

class PedidoViewset(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


def home(request):
    return render(request, 'WebApp/home.html')


def tienda(request):
    data = {
        'form':PedidoForm()
    }
    if request.method == 'POST':
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pedido registrado exitosamente")
            #data['mensaje'] = "Pedido guardado correctamente"
        else:
            data['form'] = formulario
            #messages.error(request, "El formulario de pedido contiene errores")
            #data['mensaje'] = "EL PEDIDO NO HA SIDO PROCESADO"
    return render(request, 'WebApp/tienda.html', data)



def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Su formulario de contacto ha sido recibido de forma exitosa")
        else:
            data['form'] = formulario

    return render(request, 'WebApp/contacto.html', data)



def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Autenticar al usario y redirigirlo al inicio logueado
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Su registro ha sido exitoso")
            return redirect(to='Home')
        else:
            data['form'] = formulario
    return render(request, 'registration/registrar.html', data)


# CRUD Pedidos

@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(pedidos, 5)
        pedidos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': pedidos,
        'paginator': paginator
    }

    return render(request, 'WebApp/listar_pedidos.html', data)


def eliminar_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    try:
        pedido.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('ListarPedidos')


def modificar_pedidos(request, id):
    pedido = Pedido.objects.get(id=id)
    data = {
        'form':PedidoForm(instance=pedido)
    }
    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            #data['mensaje'] = "Registro modificado correctamente"
            #data['form'] = formulario
            return redirect('ListarPedidos')
        else:
            data['form'] = formulario

    return render(request, 'WebApp/modificar_pedidos.html', data)


def login_facebook_error(request):
    return render(request, 'registration/login_facebook_error.html')
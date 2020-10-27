from django.shortcuts import render
from .forms import CustomUserForm, PedidoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Pedido
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request, 'WebApp/home.html')

@login_required
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
    return render(request, 'WebApp/contacto.html')



def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Autenticar al usario y redirigirlo al inicio logueado
            #username = formulario.cleaned_data('username')
            #password = formulario.cleaned_data('password1')
            #user = authenticate(username=username, password=password)
            #login(request, user)
            #return redirect(to='home')
    return render(request, 'registration/registrar.html', data)


# CRUD Pedidos

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'WebApp/listar_pedidos.html', {
        'pedidos':pedidos
    })

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
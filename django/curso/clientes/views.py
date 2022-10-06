from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from clientes.models import Clientes,ClientesForm

@login_required(login_url="login_page")
def index(request):
    clientes = Clientes.objects.all()
    return render(request,'index_cliente.html',{
        'clientes': clientes
    })

@login_required(login_url="login_page")
def crear_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            cliente = Clientes(
                nombre=data_form.get('nombre'),
                tipo_documento=data_form.get('tipo_documento'),
                num_documento=data_form.get('num_documento'),
                email=data_form.get('email'),
                descripcion=data_form.get('descripcion'),
            )
            cliente.save()
            return redirect('index_cliente')
    form = ClientesForm()
    return render(request, 'formulario_cliente.html',{
        'title':'Crear Cliente',
        'form':form,
    })

@login_required(login_url="login_page")
def modificar_cliente(request,id):
    cliente = Clientes.objects.get(pk=id)
    if request.method == 'POST':
        form = ClientesForm(request.POST,instance=cliente)
        if form.is_valid():
            data_form = form.cleaned_data
            cliente.nombre=data_form.get('nombre')
            cliente.tipo_documento=data_form.get('tipo_documento')
            cliente.num_documento=data_form.get('num_documento')
            cliente.email=data_form.get('email')
            cliente.descripcion=data_form.get('descripcion')
            cliente.save()
            return redirect('index_cliente')
    form = ClientesForm(instance=cliente)
    return render(request, 'formulario_cliente.html', {
        'title': 'Modificar Cliente',
        'form': form,
    })

def eliminar_cliente(request,id):
    cliente = Clientes.objects.get(pk=id)
    cliente.delete()
    return redirect('index_cliente')
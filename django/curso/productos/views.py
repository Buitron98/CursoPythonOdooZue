from django.shortcuts import render, redirect
from django.http import HttpResponse
from productos.models import Productos,ProductosForm
from clientes.models import Clientes

def index_producto(request):
    productos = Productos.objects.all()
    return render(request,'index_productos.html',{
        'productos': productos
    })

def crear_producto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            print(request.POST.get('cliente'))
            cliente = Clientes.objects.get(pk=request.POST.get('cliente'))
            producto = Productos(
                codigo=data_form.get('codigo'),
                nombre=data_form.get('nombre'),
                cantidad=data_form.get('cantidad'),
                imagen=data_form.get('imagen'),
                cliente=cliente,
                precio=data_form.get('precio'),
                descripcion=data_form.get('descripcion'),
            )
            producto.save()
            return redirect('index_producto')
    form = ProductosForm()
    return render(request, 'formulario_productos.html',{
        'title':'Crear Producto',
        'form':form,
    })

# def modificar_cliente(request,id):
#     cliente = Clientes.objects.get(pk=id)
#     if request.method == 'POST':
#         form = ClientesForm(request.POST,instance=cliente)
#         if form.is_valid():
#             data_form = form.cleaned_data
#             cliente.nombre=data_form.get('nombre')
#             cliente.tipo_documento=data_form.get('tipo_documento')
#             cliente.num_documento=data_form.get('num_documento')
#             cliente.email=data_form.get('email')
#             cliente.descripcion=data_form.get('descripcion')
#             cliente.save()
#             return redirect('index_cliente')
#     form = ClientesForm(instance=cliente)
#     return render(request, 'formulario_cliente.html', {
#         'title': 'Modificar Cliente',
#         'form': form,
#     })

# def eliminar_cliente(request,id):
#     cliente = Clientes.objects.get(pk=id)
#     cliente.delete()
#     return redirect('index_cliente')
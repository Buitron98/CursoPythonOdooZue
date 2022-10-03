from django.shortcuts import render, redirect
from django.http import HttpResponse
from facturas.models import Factura_Encabezado,Factura_Detalle,FacturaForm
from clientes.models import Clientes
from productos.models import Productos

def index_factura(request):
    facturas = Factura_Encabezado.objects.all()
    return render(request,'index_factura.html',{
        'facturas': facturas
    })

def crear_factura(request):
    form = FacturaForm()
    return render(request, 'formulario_factura.html',{
        'title':'Crear Factura',
        'form':form,
    })

# def crear_producto(request):
#     if request.method == 'POST':
#         form = ProductosForm(request.POST, request.FILES)
#         if form.is_valid():
#             data_form = form.cleaned_data
#             print(request.POST.get('cliente'))
#             cliente = Clientes.objects.get(pk=request.POST.get('cliente'))
#             producto = Productos(
#                 codigo=data_form.get('codigo'),
#                 nombre=data_form.get('nombre'),
#                 cantidad=data_form.get('cantidad'),
#                 imagen=data_form.get('imagen'),
#                 cliente=cliente,
#                 precio=data_form.get('precio'),
#                 descripcion=data_form.get('descripcion'),
#             )
#             producto.save()
#             return redirect('index_producto')
#     form = ProductosForm()
#     return render(request, 'formulario_productos.html',{
#         'title':'Crear Producto',
#         'form':form,
#     })


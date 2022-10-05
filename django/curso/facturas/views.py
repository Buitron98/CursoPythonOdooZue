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
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            #Guardar encabezado
            cliente = Clientes.objects.get(pk=request.POST.get('rel_cliente'))
            factura = Factura_Encabezado(
                fecha_factura=data_form.get('fecha_factura'),
                rel_cliente=cliente,
                precio_total=data_form.get('precio_total'),
                observaciones=data_form.get('observaciones'),
            )
            factura.save()
            #Guardar detalle
            agregar_item = True
            i = 1
            while agregar_item:
                if request.POST.get('rel_producto_'+str(i),False):
                    producto = Productos.objects.get(pk=request.POST.get('rel_producto_'+str(i)))
                    factura_detalle = Factura_Detalle(
                        rel_factura=factura,
                        rel_producto=producto,
                        cantidad=request.POST.get('cantidad_'+str(i)),
                        precio_unitario=request.POST.get('precio_unitario_'+str(i)),
                        precio_total=request.POST.get('precio_total_'+str(i)),
                    )
                    factura_detalle.save()
                else:
                    agregar_item = False
                i += 1
            return redirect('index_factura')
    form = FacturaForm()
    productos = Productos.objects.all()
    return render(request, 'formulario_factura.html',{
        'title':'Crear Factura',
        'form':form,
        'productos':productos,
    })

def modificar_factura(request,id):
    factura = Factura_Encabezado.objects.get(pk=id)
    factura_detalle = Factura_Detalle.objects.filter(rel_factura=factura)
    if request.method == 'POST':
        form = FacturaForm(request.POST,instance=factura)
        if form.is_valid():
            data_form = form.cleaned_data
            #Guardar encabezado
            cliente = Clientes.objects.get(pk=request.POST.get('rel_cliente'))
            factura.fecha_factura=data_form.get('fecha_factura')
            factura.rel_cliente=cliente
            factura.precio_total=data_form.get('precio_total')
            factura.observaciones=data_form.get('observaciones')
            factura.save()
            #Guardar detalle
            factura_detalle.delete()
            agregar_item = True
            i = 1
            while agregar_item:
                if request.POST.get('rel_producto_'+str(i),False):
                    producto = Productos.objects.get(pk=request.POST.get('rel_producto_'+str(i)))
                    item_detalle = Factura_Detalle(
                        rel_factura=factura,
                        rel_producto=producto,
                        cantidad=request.POST.get('cantidad_'+str(i)),
                        precio_unitario=request.POST.get('precio_unitario_'+str(i)),
                        precio_total=request.POST.get('precio_total_'+str(i)),
                    )
                    item_detalle.save()
                else:
                    agregar_item = False
                i += 1
            return redirect('index_factura')
    form = FacturaForm(instance=factura)
    productos = Productos.objects.all()
    return render(request, 'formulario_factura.html', {
        'title': 'Modificar factura',
        'form': form,
        'productos':productos,
        'detalles':factura_detalle,
    })

def eliminar_factura(request,id):
    factura = Factura_Encabezado.objects.get(pk=id)
    factura_detalle = Factura_Detalle.objects.filter(rel_factura=factura)
    factura_detalle.delete()
    factura.delete()
    return redirect('index_factura')
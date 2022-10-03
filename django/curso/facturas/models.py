from django.db import models
from django import forms
from django.forms import ModelForm

class Factura_Encabezado(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_factura = models.DateField(verbose_name='Fecha', default='1900-01-01')
    rel_cliente = models.ForeignKey('clientes.clientes', verbose_name='Cliente', on_delete=models.RESTRICT)
    precio_total = models.DecimalField(verbose_name='Gran Total', max_digits=15, decimal_places=2)
    observaciones = models.TextField(verbose_name='Observaciones')

class Factura_Detalle(models.Model):
    rel_factura = models.ForeignKey('facturas.factura_encabezado', verbose_name='Factura', on_delete=models.RESTRICT)
    rel_producto = models.ForeignKey('productos.productos', verbose_name='Producto', on_delete=models.RESTRICT)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio_unitario = models.DecimalField(verbose_name='Precio unitario', max_digits=15, decimal_places=2)
    precio_total = models.DecimalField(verbose_name='Total', max_digits=15, decimal_places=2)

class FacturaForm(ModelForm):
    class Meta:
        model = Factura_Encabezado
        fields = '__all__'
        widgets = {
            'fecha_factura': forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_factura'].widget.attrs['class'] = 'form-control'
        self.fields['rel_cliente'].widget.attrs['class'] = 'form-control'
        self.fields['precio_total'].widget.attrs['class'] = 'form-control'
        self.fields['observaciones'].widget.attrs['class'] = 'form-control'
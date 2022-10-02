from django.db import models
from django.forms import ModelForm

class Productos(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, primary_key=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=200)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    imagen = models.ImageField(verbose_name='Imagen', default='null', null=True, upload_to="img_productos")
    cliente = models.ForeignKey('clientes.clientes', on_delete=models.RESTRICT, verbose_name='Cliente')
    precio = models.DecimalField(verbose_name='Precio', max_digits=15, decimal_places=2)
    descripcion = models.TextField(verbose_name='Descripción')

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        #fields = ['nombre','tipo_documento','num_documento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['cantidad'].widget.attrs['class'] = 'form-control'
        self.fields['imagen'].widget.attrs['class'] = 'form-control'
        self.fields['cliente'].widget.attrs['class'] = 'form-control'
        self.fields['precio'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'

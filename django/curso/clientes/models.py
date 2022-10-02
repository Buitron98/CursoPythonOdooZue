from django.db import models
from django.forms import ModelForm

class Clientes(models.Model):
    TIPO_DOCUMENTOS = (
        ('NI','NIT'),
        ('CC','Cedula de ciudadania'),
        ('PA','Pasaporte'),
        ('OT', 'Otro'),
    )
    nombre = models.CharField(verbose_name='Nombre',max_length=100)
    tipo_documento = models.CharField(verbose_name='Tipo de documento',max_length=2, choices=TIPO_DOCUMENTOS)
    num_documento = models.CharField(verbose_name='Número de documento',max_length=20)
    email = models.EmailField(verbose_name='Email',max_length=100)
    descripcion = models.TextField(verbose_name='Descripción')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.tipo_documento}-{self.num_documento} | {self.nombre}"

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        #fields = ['nombre','tipo_documento','num_documento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_documento'].widget.attrs['class'] = 'form-control'
        self.fields['num_documento'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'



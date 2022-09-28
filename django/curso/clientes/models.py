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


class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        #fields = ['nombre','tipo_documento','num_documento']



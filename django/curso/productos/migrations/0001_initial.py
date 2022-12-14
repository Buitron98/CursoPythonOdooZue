# Generated by Django 4.1.1 on 2022-09-29 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Código')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('imagen', models.ImageField(default='null', null=True, upload_to='img_productos', verbose_name='Imagen')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Precio')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='clientes.clientes', verbose_name='Cliente')),
            ],
        ),
    ]

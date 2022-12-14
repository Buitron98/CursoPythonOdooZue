"""curso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from ingreso import views as vi
from clientes import views as vc
from productos import views as vp
from facturas import views as vf

urlpatterns = [
    path('admin/', admin.site.urls),
    #Ingreso
    path('register/', vi.register_user, name='register_user'),
    path('login/', vi.login_page, name='login_page'),
    path('logout/', vi.logout_user, name='logout_page'),
    #Clientes
    path('index_cliente/', vc.index, name='index_cliente'),
    path('crear_cliente/', vc.crear_cliente, name='crear_cliente'),
    path('modificar_cliente/<int:id>', vc.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:id>', vc.eliminar_cliente, name='eliminar_cliente'),
    #Productos
    path('index_producto/', vp.index_producto, name='index_producto'),
    path('crear_producto/', vp.crear_producto, name='crear_producto'),
    #Facturas
    path('index_factura/', vf.index_factura, name='index_factura'),
    path('crear_factura/', vf.crear_factura, name='crear_factura'),
    path('modificar_factura/<int:id>', vf.modificar_factura, name='modificar_factura'),
    path('eliminar_factura/<int:id>', vf.eliminar_factura, name='eliminar_factura'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Ajuste Portal Administraci??n
admin.site.site_title = 'Administraci??n Curso Python'
admin.site.site_header = 'Administraci??n Curso Python'
admin.site.index_title = 'Panel de gesti??n'
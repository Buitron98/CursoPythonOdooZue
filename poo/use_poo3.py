from clase7 import Persona, Cliente, Proveedor, UsuarioFinal

# persona1 = Persona()
#
# persona1.setNombre('Luis')
# persona1.setNum_documento('123456789')
# persona1.setEdad(23)
# persona1.setNacionalidad('Colombiano')
#
# persona1.info_persona()

print('########################## CLIENTE #################################')

cliente1 = Cliente()

cliente1.setNombre('Luis')
cliente1.setNum_documento('123456789')
cliente1.setEdad(23)
cliente1.setNacionalidad('Colombiano')

cliente1.setNum_compras(3)
cliente1.setRut('ABC123')
cliente1.setInfo_adicional(razon_social='Pepito S.A.S', valor_invertido=500000)

cliente1.info_persona()
#print(cliente1.getInfo_adicional())

print('########################## USUARIO FINAL #################################')

usuario1 = UsuarioFinal()

usuario1.setNombre('Luis')
usuario1.setNum_documento('123456789')
usuario1.setEdad(23)
usuario1.setNacionalidad('Colombiano')
usuario1.setNum_compras(3)
usuario1.setRut('ABC123')
usuario1.setInfo_adicional(razon_social='Pepito S.A.S', valor_invertido=500000)

usuario1.setUsername('Test')
usuario1.setPassword('PasswordTest')

usuario1.info_persona()

'''

print('########################## PROVEEDOR #################################')

proveedor1 = Proveedor()
proveedor1.setNombre('Pepito')
proveedor1.setNum_documento('789456123')
proveedor1.setEdad(42)
proveedor1.setNacionalidad('Colombiano')

proveedor1.setNum_ventas(8)
proveedor1.setInfo_adicional(razon_social='Pepito S.A.S', valor_invertido=800000)

proveedor1.info_persona()

'''

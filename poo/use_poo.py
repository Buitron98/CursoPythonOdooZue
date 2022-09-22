from clase4 import Cliente,Factura

clientes = []

print('########### Registrar Clientes #####################')
cant_clientes = int(input('Cant. Clientes a registrar: '))

i = 1
while i <= cant_clientes:
    print(f'------------ Ingrese los datos del cliente #{i} ----------------')
    identificacion = input('Digite su identificacion: ')
    nombre = input('Digite su nombre: ')
    create_cliente = Cliente(identificacion,nombre)
    clientes.append(create_cliente)
    i += 1

print('----------------------------- CREAR FACTURA -----------------------------------')

numero = input('Digite el número de la factura: ')
fecha = input('Digite la fecha: ')
i = 0
for client in clientes:
    print('ID '+str(i))
    client.info_cliente()
    i += 1
id_cliente = int(input('Digite el ID del cliente de la factura: '))
valor_total = float(input('Digite el valor total de la factura: '))

factura_uno = Factura()
factura_uno.setNumero(numero)
factura_uno.setFecha(fecha)
factura_uno.setCliente(clientes[id_cliente])
factura_uno.setValor_total(valor_total)

factura_uno.info_factura()















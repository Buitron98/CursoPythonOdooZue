
class Cliente:
    identificacion = ''
    nombre = ''
    info_adicional = {}

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getIdentificacion(self):
        return self.identificacion

    def setIdentificacion(self,identificacion):
        self.identificacion = identificacion

    def __init__(self,identificacion,nombre,**kw):
        self.identificacion = identificacion
        self.nombre = nombre
        self.info_adicional = kw

    def info_cliente(self):
        print(f'\tIdentificación: {self.identificacion}')
        print(f'\tNombre: {self.nombre}')
        print(f'\tInfo Adicional: {str(self.info_adicional)}')

class Factura:
    numero = 0
    fecha = ''
    cliente = Cliente('','')
    valor_total = 0

    # def __int__(self,numero,fecha,cliente,valor_total):
    #     self.numero = numero
    #     self.fecha = fecha
    #     self.cliente = cliente
    #     self.valor_total = valor_total

    # Getter y Setter

    def getNumero(self):
        return self.numero

    def setNumero(self,numero):
        self.numero = numero

    def getFecha(self):
        return self.fecha

    def setFecha(self,fecha):
        self.fecha = fecha

    def getCliente(self):
        return self.cliente

    def setCliente(self,cliente):
        self.cliente = cliente

    def getValor_total(self):
        return self.valor_total

    def setValor_total(self,valor_total):
        self.valor_total = valor_total

    #Funcionalidades

    def info_factura(self):
        print(f'################## INFO FACTURA #{self.numero} #######################')
        print(f'Fecha: {self.fecha}')
        print(f'Cliente:')
        self.cliente.info_cliente()
        print(f'Valor: {self.valor_total}')
        print(f'#########################################')

class Coche:

    color = ''
    marca = ''
    modelo = 0
    velocidad = 0

    def __init__(self,color,marca,modelo,velocidad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        if self.velocidad == 0:
            print('El coche ya esta totalmente quieto')
        else:
            self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad






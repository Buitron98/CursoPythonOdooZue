
class Persona:
    num_documento = ''
    nombre = ''
    edad = 0
    nacionalidad = ''

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNum_documento(self):
        return self.num_documento

    def setNum_documento(self,num_documento):
        self.num_documento = num_documento

    def getEdad(self):
        return self.edad

    def setEdad(self,edad):
        self.edad = edad

    def getNacionalidad(self):
        return self.nacionalidad

    def setNacionalidad(self,nacionalidad):
        self.nacionalidad = nacionalidad

    def info_persona(self):
        print(f'\tDocumento: {self.num_documento}')
        print(f'\tNombre: {self.nombre}')
        print(f'\tEdad: {self.edad}')
        print(f'\tNacionalidad: {self.nacionalidad}')

#Herencia estandar
class Cliente(Persona):
    num_compras = 0
    rut = ''
    info_adicional = {}

    def getNum_compras(self):
        return self.num_compras

    def setNum_compras(self,num_compras):
        self.num_compras = num_compras

    def getRut(self):
        return self.rut

    def setRut(self,rut):
        self.rut = rut

    def getInfo_adicional(self):
        return self.info_adicional

    def setInfo_adicional(self,**kw):
        self.info_adicional = kw

    def info_persona(self):
        super().info_persona()
        print(f'\tRUT: {self.rut}')
        print(f'\tNúmero de compras: {self.num_compras}')
        print(f'\tInformación adicional: {self.info_adicional}')

#Herencia Multinivel
class UsuarioFinalC(Cliente):
    username = ''
    password = ''

    def getUsername(self):
        return self.username

    def setUsername(self,username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self,password):
        self.password = password

    def info_persona(self):
        super().info_persona()
        print(f'\tUsername: {self.username}')
        print(f'\tPassword: {self.password}')

class Proveedor(Persona):
    num_ventas = 0
    info_adicional = {}

    def getNum_ventas(self):
        return self.num_ventas

    def setNum_ventas(self, num_ventas):
        self.num_ventas = num_ventas

    def getInfo_adicional(self):
        return self.info_adicional

    def setInfo_adicional(self,**kw):
        self.info_adicional = kw

    def info_persona(self):
        super().info_persona()
        print(f'\tNúmero de ventas: {self.num_ventas}')
        print(f'\tInformación adicional: {self.info_adicional}')

#Herencia multiple
class Suma:
    def sumar(self,num1,num2):
        return num1+num2

class Resta:
    def restar(self,num1,num2):
        return num1-num2

class Multiplicar:
    def multiplicar(self,num1,num2):
        return num1*num2

class Dividir:
    def dividir(self,num1,num2):
        return num1/num2

class Calculadora(Suma,Resta,Multiplicar,Dividir):
    num1=0
    num2=0

    def getNum1(self):
        return self.num1

    def setNum1(self,num1):
        self.num1 = num1

    def getNum2(self):
        return self.num2

    def setNum2(self,num2):
        self.num2 = num2

    def __del__(self):
        print('Usted destruyo este objeto.')


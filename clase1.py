'''
# Mostrar mensaje en consola
print('Hola Mundo!')
#Solicitar valor por consola
nombre = input('Escribe tu nombre: ')
print(nombre)
'''

################### TIPOS DE DATOS EN PYTHON
nada = None
cadena_texto = 'Texto fijo'
print(cadena_texto)
entero = 85
flotante_decimal = 3.14
booleano = True
tupla = (1,2,3)
diccionario = {
    'nombre':'Luis',
    'apellido':'Buitron',
    'edad':23,
    'nacionalidad':'Colombiano'
}

################### CONCATENAR CADENAS TEXTOS
nombre = 'Luis'
apellido = 'Buitron'
nacionalidad = 'Colombiano'

#1 Forma
texto = 'Nombre:'+nombre+'\nApellido:'+apellido+'\nNacionalidad:'+nacionalidad
#print(texto)
#2 Forma
texto = f'Nombre:{nombre}\nApellido:{apellido}\nNacionalidad:{nacionalidad}'
#print(texto)
#3 Forma
texto = 'Nombre:{}\nApellido:{}\nNacionalidad:{}'.format(nombre,apellido,nacionalidad)
#print(texto)

################### CONVERTIR DE UN TIPO DE DATO A OTRO

#edad = input('Porfavor digite su edad: ')
#edad = int(edad)+20
'''
int(edad)
str(edad)
float(edad)
'''
#print(type(edad))
#print(f'En 20 años, tendras {edad} años')

################### OPERADORES Y ESTRUCTURAS DE CONTROL

# - Operadores aritmeticos (+, -, *, / , %, ^)
# - Operadores de comparación (<, >, <= , >= , =, !=)
# - Operadores lógicos (and, or, in, not in)

#Estructuras de control (if, while, for)

#Ejemplo 1 IF
edad = int(input('Porfavor digite su edad: '))
if edad >= 18 and edad < 80:
    print('Usted es un adulto')
elif edad >= 80:
    print('Usted tiene mas de 80 años.')
else:
    print('Usted es menor de edad')
print('Fin ejecución')

#Ejemplo 2 WHILE
nombre = ''
while nombre != 'luis':
    nombre = input('Digite su nombre: ')
    if nombre != 'luis':
        print('Su nombre es incorrecto!')
    else:
        print('Su nombre es correcto!')

#Ejemplo 3 FOR
for item in range(1,10):
    print(item)

for item in range(1,11):
    print(f'################## TABLA DE MULTIPLICAR {item} ##############')
    for multi in range(1,11):
        print(f"{item} * {multi} = {item*multi}")

#Ejemplo 4
lst_numeros = []
while len(lst_numeros) < 5:
    numero = int(input('Digite un número: '))
    if numero not in lst_numeros:
        lst_numeros.append(numero)
    else:
        lst_numeros.remove(numero)
    print(lst_numeros)
longitud_lst_numeros = len(lst_numeros)












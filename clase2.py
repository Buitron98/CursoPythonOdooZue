import pandas as pd

def tablaMultiplicar(item,limit=10):
    #global nombre
    #nombre = 'Luis'
    for multi in range(1, limit+1):
        print(f"{item} * {multi} = {item * multi}")
    #print('DENTRO DE LA FUNCIÓN: '+nombre)


'''
continuar = True
while continuar:
    numero = int(input('Digite un numero: '))
    limite = int(input('Digite el limite a multiplicar: '))
    tablaMultiplicar(numero,limite)
    pregunta = int(input('Digite 0 si desea continuar o 1 si quiere salir: '))
    continuar = True if pregunta == 0 else False
print('Termino la ejecución')
'''

#tablaMultiplicar(5)
#print('FUERA DE LA FUNCIÓN: '+nombre)

'''
Diccionario:
Es un tipo de datos que almacena un conjunto de datos
En formato clave: valor
Estructura como un Json
'''

persona_datos_adicionales = {
    'fecha_nacimiento':'13/11/1998',
    'cargo': 'Ingeniero de Software',
    'empresa': 'ZUE'
}

persona = {
    'nombre':'Luis',
    'apellido':'Buitron',
    'edad':23,
    'nacionalidad':'Colombiano',
    'mayor_edad': True,
    'comidas_favoritas': ['Colombiana','Mexicana','Italiana'],
    'datos_adicionales': persona_datos_adicionales
}
#print(persona)

'''
todos_datos_persona = {**persona,**persona_datos_adicionales}
print(todos_datos_persona)
todos_datos_persona['identificacion'] = '123456789'
todos_datos_persona.pop('mayor_edad')
print(todos_datos_persona)
'''

cant_personas = 2
lst_personas = []
while len(lst_personas) < cant_personas:
    nombre = input('Digite su nombre: ')
    apellido = input('Digite su apellido: ')
    edad = int(input('Digite su edad: '))
    persona = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
    }
    lst_personas.append(persona)
'''
print('################################')
print(lst_personas)
for persona in lst_personas:
    print('################################')
    print(persona)
    print('Edad: '+str(persona.get('edad', 'No se encontro la edad')))
'''
print(pd.DataFrame(lst_personas))

# Manejo de errores
'''
try:
    numero = input('Digite su numero: ')
    numero = '2' + int(numero)
    print(numero)
except Exception as e:
    print(e)
    if str(e).find('concatenate') > -1:
        print('No se logro concatenar la información')
'''



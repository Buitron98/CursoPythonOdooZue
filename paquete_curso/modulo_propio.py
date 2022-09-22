def tablaMultiplicar(item,limit=10):
    for multi in range(1, limit+1):
        print(f"{item} * {multi} = {item * multi}")

def holaMundo(nombre):
    print(f'Hola Mundo {nombre}')

def calculadora(numero1,numero2):
    print(f'Suma: {numero1 + numero2}')
    print(f'Resta: {numero1 - numero2}')
    print(f'Multiplicacion: {numero1 * numero2}')
    print(f'Division: {numero1 / numero2}')
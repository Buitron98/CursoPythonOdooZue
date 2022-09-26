
def upper_texto(function):
    def wrapper():
        func = function()
        texto_upper = func.upper()
        #print('Esta usando un decorador')
        return texto_upper
    return wrapper

@upper_texto
def hola_mundo():
    return 'hola mundo'

@upper_texto
def hola_mundo2():
    return 'hola mundo 2'

@upper_texto
def hola_mundo3():
    return 'hola mundo 3'

print(hola_mundo())
print(hola_mundo2())
print(hola_mundo3())
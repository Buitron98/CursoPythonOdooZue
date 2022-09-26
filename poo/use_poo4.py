from clase7 import Calculadora


calculadora1 = Calculadora()

calculadora1.setNum1(5)
calculadora1.setNum2(2)

print('Número 1: '+str(calculadora1.getNum1()))
print('Número 2: '+str(calculadora1.getNum2()))

print(calculadora1.sumar(calculadora1.getNum1(),calculadora1.getNum2()))
print(calculadora1.restar(calculadora1.getNum1(),calculadora1.getNum2()))
print(calculadora1.multiplicar(calculadora1.getNum1(),calculadora1.getNum2()))
print(calculadora1.dividir(calculadora1.getNum1(),calculadora1.getNum2()))

del calculadora1

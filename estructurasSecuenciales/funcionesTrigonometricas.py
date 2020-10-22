#Resolver un problema para conocer los siguientes datos: nombre (cambiar a mayúsculas
#e imprimir la longitud), numero (calcular el coseno, la tangente y el seno
import math

nombre = str(input("Ingrese nombre: "))
numero = float(input("Ingrese un número: "))
numeroRadianes = math.radians(numero)

seno = math.sin(numeroRadianes)
coseno = math.cos(numeroRadianes)
tangente = math.tan(numeroRadianes)

print('El seno de {} es: {}'.format(numero, seno))
print('El coseno de {} es: {}'.format(numero, coseno))
print('La tangente de {} es: {}'.format(numero, tangente))
print('Tu nombres es {} y tiene una longitud de {} caracteres'.format(nombre.upper(), len(nombre)))
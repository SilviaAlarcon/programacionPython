""" 4. Resolver un problema para calcular la suma de los primeros cien números e imprimirla.
La ejecución debe tener una salida similar a la siguiente:
La suma de los 100 números es: 5050 """

numeros = range(1, 101)
suma = 0

for i in numeros:
    suma += i
    i += 1
print('La suma de los 100 numeros es {}'.format(suma))
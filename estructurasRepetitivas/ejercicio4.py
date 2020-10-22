""" 4. Resolver un problema para calcular la suma de los primeros cien números e imprimirla.
La ejecución debe tener una salida similar a la siguiente:
La suma de los 100 números es: 5050 """

suma = 0

for i in range(1, 101):
    suma += i
  
print('La suma de los 100 numeros es {}'.format(suma))
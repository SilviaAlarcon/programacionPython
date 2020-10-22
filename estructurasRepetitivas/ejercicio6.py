""" 6. Resolver un problema que muestre los números comprendidos entre un número definido 
por el usuario y 100, además los muestra en intervalos de 10 en 10. 
La ejecución pide un dato y debe tener una salida similar a la siguiente:
Dame un número entre 1 y 99= 50
Números del 50 al 100 
50
60
70
80 
90 
100 """

numero = int(input('Dame un número entre 1 y 99: '))

print('Numeros del {} al 100'.format(numero))

for i in range(numero, 101, 10):
    print(i)
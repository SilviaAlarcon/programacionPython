""" 2. Resolver un problema que imprima y calcule la suma de los n números que ingrese 
    el usuario. La ejecución pide datos y debe tener una salida similar a la siguiente:
Cuantos números=6 
1
2
3
4 
5 
6
La suma de los 6 números es: 21 """

numeroUsuario = int(input('Cuantos numeros: '))

suma, contador = 0, 1

while contador <= numeroUsuario:
    print(contador)
    suma += contador
    contador += 1
print('La suma de los {} numeros es {}'.format(numeroUsuario, suma))
""" 5. Resolver un problema que pida al usuario una tabla de multiplicar y la muestre. 
La ejecución debe tener una salida similar a la siguiente:
Dame una tabla= 4 
Tabla del 4
4 x 1= 4
4 x 2= 8
4 x 3 = 12 
4 x 4 = 16 
4 x 5 = 20 
4 x 6 = 24 
4 x 7 = 28 
4 x 8 = 32 
4 x 9 = 36 
4 x 10 = 40 """

tabla = int(input('Dame una tabla: '))
resultado = 0

print('Tabla del {}'.format(tabla))

for i in range(1, 11):
    resultado = tabla * i
    print('{} x {} = {}'.format(tabla, i, resultado))
    i += 1
""" 3. Resolver un problema que determine la media de una lista indefinida de números positivos 
ingresados por el usuario, este debe terminar cuando se ingresa un número negativo. 
La ejecución pide datos y debe tener una salida similar a la siguiente:
Ingrese un número:3 
Ingrese un número:4 
Ingrese un número:5 
Ingrese un número: -7
La media es: 4.0 """

#MEDIA FORMA 1
""" import statistics as stats

numeroUsuario = int(input('Ingrese un numero: '))
lista = [numeroUsuario]

while numeroUsuario > 0:
    numeroUsuario = int(input('Ingrese un numero: '))
    if numeroUsuario > 0:
        lista.append(numeroUsuario)
    else:
        print('Resultado listo')
media = stats.mean(lista)

print('La media es {}'.format(media)) """


#MEDIA FORMA 2
""" numeroUsuario = int(input('Ingrese un numero: '))
lista = [numeroUsuario]
suma = numeroUsuario

while numeroUsuario > 0:
    numeroUsuario = int(input('Ingrese un numero: '))
    if numeroUsuario > 0:
        suma += numeroUsuario
        lista.append(numeroUsuario)
    else:
        print('Resultado listo')
print(lista)
longitud = int(len(lista))
media = suma / longitud

print('La media es {}'.format(media)) """

#MEDIA FORMA 3
numeroUsuario = int(input('Ingrese un numero: '))
contador = 1
suma = numeroUsuario

while numeroUsuario > 0:
    numeroUsuario = int(input('Ingrese un numero: '))
    if numeroUsuario > 0:
        suma += numeroUsuario
        contador += 1
    else:
        print('Resultado listo')

media = suma / contador

print('La media es {}'.format(media))

#OBTENER LA MEDIANA
""" mediana = int(input('Ingrese un numero: '))

lista = [mediana]

while mediana > 0:
    mediana = int(input('Ingrese un numero: '))
    lista.append(mediana)


lista = sorted(lista)
print(lista)
n = len(lista)
if n%2 == 1:
    print('La mediana es {}'.format(lista[n//2]))
else:
    i = n//2
    print('La mediana es {}'.format((lista[i - 1] + lista[i])/2)) """
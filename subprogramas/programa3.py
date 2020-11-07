import math

'''Función sin argumentos para imprimir el siguiente menú:
    MENU
    1 - SENO
    2 - COSENO
    3 - TANGENTE
'''
def menu():
    print('MENÚ \n 1 - SENO \n 2 - COSENO \n 3 - TANGENTE')

#Función con un argumento que devuelva el seno de un valor
def seno(numero):
    numero_flotante = float(numero)
    numero_en_radianes = math.radians(numero_flotante)
    return math.sin(numero_en_radianes)

'''Función sin argumentos que pida un número entero e imprima el seno ( llamando
a la función anterior 2).'''
def seno_usuario():
    numero = int(input('Dame un entero: '))
    print(f'El seno de {numero} es {round(seno(numero), 5)}')

#Función con un argumento que retorne el coseno de un valor 
def coseno(numero):
    numero_flotante = float(numero)
    numero_en_radianes = math.radians(numero_flotante)
    return math.cos(numero_en_radianes)

'''Función sin argumentos que pida un número entero e imprima el coseno ( llamando
a la función anterior 4)'''
def coseno_usuario():
    numero = int(input('Dame un entero: '))
    print(f'El coseno de {numero} es {round(coseno(numero), 5)}')

#Función con un argumento que retorne la tangente de un valor 
def tangente(numero):
    numero_flotante = float(numero)
    numero_en_radianes = math.radians(numero_flotante)
    return math.tan(numero_en_radianes)

'''Función sin argumentos que pida un número entero e imprima la tangente
(llamando a la función anterior 6)'''
def tangente_usuario():
    numero = int(input('Dame un entero: '))
    print(f'La tangente de {numero} es {round(tangente(numero), 5)}')

'''Función principal sin argumentos donde el programa muestra el menú, si se elige
una opción válida, muestra la operación seleccionada y termina, de lo contrario
manda un mensaje de “Opción inválida” y vuelve a pedir una opción válida.
En cada opción solo se hace la llamada a una función ( 3, 5 y 7), NO se realiza
ninguna operación. Además, se ocupan las funciones de la biblioteca math (pi,
seno, coseno, tangente).'''
def main():
    while True:
        menu()
        opcion = int(input('Selecciona una opción: '))

        if opcion == 1:
            seno_usuario()
            break
        elif opcion == 2:
            coseno_usuario()
            break
        elif opcion == 3:
            tangente_usuario()
            break
        else:
            print('Opción inválida \n')

if __name__ == '__main__':
    #Al final solo se invoca a la función principal. 
    main()
